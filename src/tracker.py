# src/tracker.py
import sqlite3
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

DB_PATH = "data/expenses.db"

def add_expense(amount, category, note, expense_date=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if not expense_date:
        expense_date = str(date.today())
    c.execute("INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
              (amount, category, note, expense_date))
    conn.commit()
    conn.close()

def get_expenses_by_date(expense_date=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if not expense_date:
        expense_date = str(date.today())
    c.execute("SELECT * FROM expenses WHERE date = ?", (expense_date,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_expenses_by_category(category):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    rows = c.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def export_expenses_to_excel():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    df.to_excel("data/expense_export.xlsx", index=False)
    conn.close()
    print("📁 Exported to data/expense_export.xlsx")

def plot_category_pie_chart():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT category, amount FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No data to plot.")
        return

    category_totals = df.groupby('category')['amount'].sum()

    plt.figure(figsize=(6,6))
    category_totals.plot.pie(autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title("Expenses by Category – Pie Chart")
    plt.ylabel("")  # remove y-axis label
    plt.tight_layout()
    plt.savefig("data/category_pie_chart.png")
    plt.show()


def plot_category_bar_chart():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT category, amount FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No data to plot.")
        return

    category_totals = df.groupby('category')['amount'].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    plt.bar(category_totals.index, category_totals.values, color='mediumseagreen')
    plt.title("Expenses by Category – Bar Chart")
    plt.xlabel("Category")
    plt.ylabel("Total Amount (₹)")
    plt.xticks(rotation=30)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig("data/category_bar_chart.png")
    plt.show()

def plot_category_horizontal_bar():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT category, amount FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No data to plot.")
        return

    category_totals = df.groupby('category')['amount'].sum().sort_values()

    plt.figure(figsize=(8, 5))
    plt.barh(category_totals.index, category_totals.values, color='cornflowerblue')
    plt.title("Expenses by Category – Horizontal Bar")
    plt.xlabel("Total Amount (₹)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.grid(axis='x')
    plt.savefig("data/category_horizontal_bar.png")
    plt.show()


