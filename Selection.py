def calculates():
    name = input("Enter employee name: ").strip().lower()
    years = int(input("Enter year-in-service: "))
    office = input("Enter Office: ").strip().upper()

    amount_bonus = {
        'IT': {'above_10': 10000, 'below_or_equal_10': 5000},
        'ACCT': {'above_10': 12000, 'below_or_equal_10': 6000},
        'HR': {'above_10': 15000, 'below_or_equal_10': 7500}
    }

    if office not in amount_bonus:
        print("Invalid office. Please enter IT, ACCT, or HR.")
        return

    if years > 10:
        bonus = amount_bonus[office]['above_10']
    else:
        bonus = amount_bonus[office]['below_or_equal_10']

    print(f"Hi {name}, your bonus is {bonus}.")

calculates()
