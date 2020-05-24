"""
Program for keeping track of finances
"""

import sqlite3


class Database:
    """
    Database parent class handles connection and disconnection from database
    Also runs table initiation statement for subclass initiation
    """

    def __init__(self, table_init_statement=""):
        self.db_connection = sqlite3.connect("finances/data/data.db")
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute(table_init_statement)
        self.db_connection.commit()

    def disconnect(self):
        """
        Disconect from the database
        This might be better to do with a context manager?
        """
        self.db_connection.close()


class Accounts(Database):
    """
    Accounts class inherits from database class to make account specific database
    This stores information about accounts such as type and intial balances
    """

    table_init_statement = """CREATE TABLE IF NOT EXISTS accounts (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE NOT NULL,
                        type TEXT NOT NULL,
                        starting_balance INTEGER DEFAULT 0,
                        current_balance INTEGER DEFAULT 0
                        );"""

    def __init__(self):
        super().__init__(Accounts.table_init_statement)

    def add(self, account_name, account_type, starting_balance):
        """
        Adds account record to database
        """
        self.db_cursor.execute(
            """INSERT INTO accounts (name, type, starting_balance)
            VALUES (:name, :type, :starting_balance);""",
            {
                "name": account_name,
                "type": account_type,
                "starting_balance": int(starting_balance * 100),
            },
        )
        self.db_connection.commit()

    def overview(self):
        """
        Provides overview for accounts, not yet fleshed out
        """
        self.db_cursor.execute("SELECT * FROM accounts")

        return self.db_cursor.fetchall()

    def update_balance(self, account_name):
        """
        Perhaps not the most elegant solution but currently calculates account balance
        when required by summing all transactions and adding to initial balance.
        This avoids discrepancy between running account total and actual transactions
        """
        self.db_cursor.execute(
            "SELECT amount FROM transactions where account_from=:account",
            {"account": account_name},
        )
        transactions_total = sum(amount[0] for amount in self.db_cursor.fetchall())
        self.db_cursor.execute(
            "SELECT starting_balance FROM accounts WHERE name=:account",
            {"account": account_name},
        )
        starting_balance = sum(balance[0] for balance in self.db_cursor.fetchall())
        current_balance = transactions_total + starting_balance
        self.db_cursor.execute(
            "UPDATE accounts SET current_balance = :current_balance WHERE name = :account;",
            {"current_balance": current_balance, "account": account_name},
        )
        self.db_connection.commit()

    def get_balance(self, account_name):
        """
        This is called when balance is requested
        Currently calculate new balance each time
        Perhaps cut out the middle man and remove the balance column?
        """
        self.update_balance(account_name)
        self.db_cursor.execute(
            "SELECT current_balance FROM accounts WHERE name=:account",
            {"account": account_name},
        )
        balance = sum(_[0] for _ in self.db_cursor.fetchall())
        return balance


class Transactions(Database):
    """
    Class inherits database class to form transactions specific database
    Stores information about transactions including catagories
    """

    table_init_statement = """CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        amount INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        account_from TEXT NOT NULL,
                        payee TEXT NOT NULL,
                        catagory TEXT NOT NULL
                        );"""

    def __init__(self):
        super().__init__(Transactions.table_init_statement)

    def add_transaction(self, amount, date, account_from, payee, catagory):
        """
        Adds a transaction record to database
        """
        self.db_cursor.execute(
            """INSERT INTO transactions (amount, date, account_from, payee, catagory)
            VALUES (:amount, :date, :account_from, :payee, :catagory);""",
            {
                "amount": amount * 100,
                "date": date,
                "account_from": account_from,
                "payee": payee,
                "catagory": catagory,
            },
        )
        self.db_connection.commit()

    def get_records(self):
        """
        Retrieves a records from database
        """
        self.db_cursor.execute("""SELECT * FROM transactions;""")
        return self.db_cursor.fetchall()


def main():
    """
    Current main function works in a commandline capacity to test functionality
    Aim to produce a flask app once logic is in place
    """

    transactions_db = Transactions()
    accounts_db = Accounts()

    print("Welcome to Finance Manager\nWhat would you like to do?\n\n")
    while True:
        print(
            "a) View transactions\nb) Add a transaction\nc) View accounts\n"
            "d) Add an account\ne) See spending overview\n"
        )
        raw_input = input(":")
        # view transactions
        if raw_input == "a":
            print(transactions_db.get_records())
        # add transaction
        elif raw_input == "b":
            amount = float(input("Amount £"))
            date = input("Date YYYY-MM-DD: ")
            account_from = input("Account: ")
            payee = input("Payee: ")
            catagory = input("Catagory: ")
            transactions_db.add_transaction(amount, date, account_from, payee, catagory)
        # view accounts
        elif raw_input == "c":
            print(accounts_db.overview())
        # add account
        elif raw_input == "d":
            account_name = input("Name: ")
            account_type = input("Type: ")
            starting_balance = int(100 * float(input("Starting balance £")))
            accounts_db.add(account_name, account_type, starting_balance)
        # spending overview
        elif raw_input == "q":
            break


if __name__ == "__main__":
    main()
