def compute_payslip():
    name = input("Employee Name: ")
    number_of_hours = float(input("Enter Number Of Hours: "))
    SSS = float(input("SSS Contribution: "))
    PhilHealth = float(input("Phil Health: "))
    HousingLoan = float(input("Housing Loan: "))

    rates_per_hour = 500.0

    Gross_salary = number_of_hours * rates_per_hour
    Tax = Gross_salary * 0.10
    Total_deduction = SSS + PhilHealth + HousingLoan + Tax
    Net_salary = Gross_salary - Total_deduction

    print("\n======PAYSLIP=======")
    print("========EMPLOYEE INFORMATION===")
    print(f"Employee Name: {name}")
    print(f"Rendered Hours: {number_of_hours}")
    print(f"Rate per Hour: {rates_per_hour}")
    print(f"Gross Salary: {Gross_salary:.1f}")
    print("========DEDUCTIONS=====")
    print(f"SSS: {SSS}")
    print(f"PhilHealth: {PhilHealth}")
    print(f"Other Loan: {HousingLoan}")
    print(f"Tax: {Tax:.1f}")
    print(f"Total Deductions: {Total_deduction:.1f}")
    print(f"\nNet Salary: PHP {Net_salary:.1f}")

compute_payslip()
