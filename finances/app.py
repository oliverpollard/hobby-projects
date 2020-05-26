"""
Flask application for finance app
"""

import io
import os
import random
import datetime

from flask import Flask, Response, redirect, render_template, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from finances import Accounts, Transactions
from forms import AddTransaction, EditTransaction

app = Flask(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def transactions_view():
    transactions_db = Transactions()

    add_transaction = AddTransaction()
    if add_transaction.validate_on_submit():
        transactions_db.add_transaction(
            add_transaction.amount.data,
            add_transaction.date.data,
            add_transaction.account.data,
            add_transaction.payee.data,
            add_transaction.catagory.data,
        )
        return redirect(url_for("transactions_view"))
    edit_transaction = EditTransaction()

    transactions = sorted(
        transactions_db.get_records(), key=lambda k: k["date"], reverse=True
    )
    return render_template(
        "index.html",
        title="Transactions",
        transactions=transactions,
        add_transaction=add_transaction,
        edit_transaction=edit_transaction,
    )


@app.route("/summary", methods=["GET", "POST"])
def summary_view():
    transactions_db = Transactions()
    catagory_info = transactions_db.get_catagory_info()
    print(catagory_info)

    return render_template("summary.html", title="Summary", catagory_info=catagory_info)


@app.context_processor
def utility_processor():
    def format_month(month_number):
        return datetime.date(1900, int(month_number), 1).strftime("%B")

    return dict(format_month=format_month)
