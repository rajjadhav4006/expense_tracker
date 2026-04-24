import pandas as pd
from db import connect

def analyze_expenses_df():class Expense:
    def __init__(self, title, amount, category, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    def to_tuple(self):
        return (self.title, self.amount, self.category, self.date)
    conn = connect()
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df
