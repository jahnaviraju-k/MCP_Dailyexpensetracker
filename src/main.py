# src/main.py
from db import init_db
from tracker import (
    add_expense, get_expenses_by_date, get_expenses_by_category,
    delete_expense, export_expenses_to_excel, plot_category_pie_chart, plot_category_bar_chart, plot_category_horizontal_bar
)


def show_menu():
    print("\n== Daily Expense Tracker ==")
    print("1. Add Expense")
    print("2. View Today's Expenses")
    print("3. View Expenses by Category")
    print("4. Delete an Expense")
    print("5. Export to Excel")
    print("6. Show Category-Wise Pie Chart")
    print("7. Show Category-wise Bar Chart")
    print("8. Show Category-Wise Horizontal Bar Chart")
    print("9. Exit")


def run():
    init_db()
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Amount (₹): "))
                category = input("Category: ")
                note = input("Note (optional): ")
                add_expense(amount, category, note)
                print("✅ Expense added.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "2":
            expenses = get_expenses_by_date()
            if expenses:
                print("\n-- Today's Expenses --")
                for e in expenses:
                    print(f"[{e[0]}] ₹{e[1]} | {e[2]} | {e[3]} | {e[4]}")
            else:
                print("No expenses for today.")
        elif choice == "3":
            category = input("Enter category: ")
            expenses = get_expenses_by_category(category)
            if expenses:
                print(f"\n-- Expenses in '{category}' --")
                for e in expenses:
                    print(f"[{e[0]}] ₹{e[1]} | {e[3]} | {e[4]}")
            else:
                print("No expenses in that category.")
        elif choice == "4":
            try:
                expense_id = int(input("Enter ID to delete: "))
                delete_expense(expense_id)
                print("🗑️ Expense deleted.")
            except ValueError:
                print("❌ Invalid ID.")
        elif choice == "5":
            export_expenses_to_excel()
        elif choice == "6":
            plot_category_pie_chart()
        elif choice == "7":
            plot_category_bar_chart()
        elif choice == "8":
            plot_category_horizontal_bar()
        elif choice == "9":
                print("👋 Goodbye!")
                break


if __name__ == "__main__":
    run()
