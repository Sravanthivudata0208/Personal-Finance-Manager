# Personal Finance Manager System

transactions = []

while True:
    print("\n===== Personal Finance Manager =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. View Transactions")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ADD INCOME
    if choice == "1":
        amount = float(input("Enter income amount: "))
        category = input("Enter income source (salary, bonus, etc): ")

        transactions.append({
            "type": "income",
            "amount": amount,
            "category": category
        })

        print("✔ Income added successfully!")

    # ADD EXPENSE
    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category (food, travel, etc): ")

        transactions.append({
            "type": "expense",
            "amount": amount,
            "category": category
        })

        print("✔ Expense added successfully!")

    # VIEW SUMMARY
    elif choice == "3":
        total_income = 0
        total_expense = 0

        for t in transactions:
            if t["type"] == "income":
                total_income += t["amount"]
            else:
                total_expense += t["amount"]

        balance = total_income - total_expense

        print("\n----- FINANCIAL SUMMARY -----")
        print("Total Income   :", total_income)
        print("Total Expense  :", total_expense)
        print("Balance        :", balance)

    # VIEW ALL TRANSACTIONS
    elif choice == "4":
        if not transactions:
            print("No transactions found!")
        else:
            print("\n----- TRANSACTIONS -----")

            for i, t in enumerate(transactions, start=1):
                print(f"{i}. {t['type'].upper()} - {t['category']} - {t['amount']}")

    # EXIT
    elif choice == "5":
        print("Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice! Try again.")