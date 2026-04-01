
import os
import datetime
class Expense:
    def __init__(self,id,category,amount,date):
        self.id=id
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"ID:{self.id}, Category:{self.category}, Amount:{self.amount}, Date:{self.date.strftime('%d-%m-%Y')}"

class ExpenseManager:
    def __init__(self,filename="expenses.txt"):
        self.filename= filename
        self.expenses = []
        self.next_id = 1
        self.load_expenses()

    # ---------- File Handling ----------

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data)==4:
                        id, category, amount, date = data
                        date=datetime.datetime.strptime(date,"%d-%m-%Y")
                        self.expenses.append(Expense(int(id),category,float(amount),date))
        if self.expenses:
            self.next_id = max(e.id for e in self.expenses) + 1

    def save_expenses(self):
        with open (self.filename,"w") as file:
            for e in self.expenses:
                file.write(f"{e.id},{e.category},{e.amount},{e.date.strftime('%d-%m-%Y')}\n")

    # ---------- Core Functionalities ----------

    def add_expenses(self):
        try:
            category=input("\nEnter Category:").strip()
            amount=float(input("Enter Amount:"))
            date=input("Enter Date (dd-mm-yyyy):").strip()
            date = datetime.datetime.strptime(date, "%d-%m-%Y")
            for e in self.expenses:
                if e.category.lower()==category.lower() and e.amount==amount and e.date==date:
                    print("This expense already exists.\n")
                    return

            self.expenses.append(Expense(self.next_id,category, amount, date))
            self.next_id += 1
            self.save_expenses()
            print("Expense added successfully!.\n")
        except ValueError:
            print("Please enter a valid data type.\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.\n")
        else:
            print("\n---Expenses List---")
            for e in self.expenses:
                print(e)
        print()

    def search_expenses(self):
        search=input("\nEnter your category:").strip()
        found = False
        for e in self.expenses:
            if search.lower() in e.category.lower() :
                print(e)
                found = True
        if not found:
            print("No expenses found.\n")
        print()

    def delete_expenses(self):

        try:
            id = int(input("Enter ID to delete: "))

            for e in self.expenses:
                if e.id == id:
                    self.expenses.remove(e)
                    self.save_expenses()  # ✅ ADD THIS
                    print("Deleted successfully")
                    return

            print("ID not found")

        except ValueError:
            print("Enter valid ID")


    def total_spending(self):
        total = 0
        for e in self.expenses:
            total += e.amount
        print("\nTotal spending:",total)
        print()

    def category_analysis(self):
        total=0

        categories=set()
        for e in self.expenses:
            categories.add(e.category)
        print("\nAvailable Categories:", list(categories))

        category = input("Enter your category you want to analyse:").strip()

        for e in self.expenses:
            if e.category.lower()==category.lower():
                total += e.amount

        if total > 0:
            print(f"Total spending of {category} is {total}.")
        else:
            print(f"Category '{category}' not found.")
        print()

    def monthly_report(self):
        try:
            total=0
            month=int(input("\nEnter Month (1-12):"))

            for e in self.expenses:
                if e.date.month==month:
                    total += e.amount

            if total > 0:
                print(f"Total spending for month {month} is {total}.")
            else:
                print("No expenses found for this month.")

        except ValueError:
            print("Please enter a valid data type.\n")
        print()

    def insights(self):
        print("\n--- Choose Insights ---")
        print("1. Monthly Category Analysis")
        print("2. Spending Trend (Month Comparison)")

        try:
            choice = int(input("\nEnter your choice(1-2): "))

 #   Insight 1: Monthly Category Analysis

            if choice == 1:
                data = {}

                for e in self.expenses:
                    month = e.date.month

                    if month not in data:
                        data[month] = {}

                    data[month][e.category] = data[month].get(e.category, 0) + e.amount

                print("\n--- Month-wise Category Analysis ---")

                for month, categories in data.items():
                    print(f"\nMonth {month}:")
                    for cat, amt in categories.items():
                        print(f"{cat} → {amt}")

#  Insight 2: Spending Trend (Month Comparison)

            elif choice == 2:
                month1 = int(input("Enter current month (1-12): "))
                month2 = int(input("Enter previous month (1-12): "))

                total1 = 0
                total2 = 0

                for e in self.expenses:
                    if e.date.month == month1:
                        total1 += e.amount
                    elif e.date.month == month2:
                        total2 += e.amount

                print(f"\nMonth {month1} Spending: {total1}")
                print(f"Month {month2} Spending: {total2}")

                if total1 > total2:
                    print("Spending increased ")
                elif total1 < total2:
                    print("Spending decreased ")
                else:
                    print("Spending is same.")

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid input.")
        print()

    # _______________Main Program__________________

def main():

    track = ExpenseManager()

    while True:

        print("======Smart Expense Tracker======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Delete Expense")
        print("5. Total Spending")
        print("6. Category Analysis")
        print("7. Monthly Report")
        print("8. Insights")
        print("9. Exit")

        choice = int(input("Enter your choice (1-9):"))

        if choice == 1:
            track.add_expenses()
        elif choice == 2:
            track.view_expenses()
        elif choice == 3:
            track.search_expenses()
        elif choice == 4:
            track.delete_expenses()
        elif choice == 5:
            track.total_spending()
        elif choice == 6:
            track.category_analysis()
        elif choice == 7:
            track.monthly_report()
        elif choice == 8:
            track.insights()
        elif choice == 9:
            print("Exiting Smart Expense Tracker...Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter one of the options 1-9")


if __name__ == "__main__":
    main()














