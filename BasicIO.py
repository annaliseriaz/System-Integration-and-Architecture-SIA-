name = input("Enter Student's Name (LN, FN, MI): ")

print("Enter Student's Grade in ")

Math = float(input("Math: "))
Science = float(input("Science: "))
English = float(input("English: "))

Avg = (Math + Science + English) / 3

print(f"Average Grade of {name} is {Avg:.2f}.")
