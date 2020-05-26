from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField,
    HiddenField,
)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length


class AddTransaction(FlaskForm):
    date = StringField("Date", validators=[DataRequired()])
    account = StringField("Account", validators=[DataRequired()])
    amount = StringField("Amount", validators=[DataRequired()])
    payee = StringField("Payee", validators=[DataRequired()])
    catagory = StringField("Catagory", validators=[DataRequired()])
    submit = SubmitField("Add")


class RemoveTransaction(FlaskForm):
    SubmitField = SubmitField("Remove")


class EditTransaction(AddTransaction):
    record_id = HiddenField("Catagory", validators=[DataRequired()])
