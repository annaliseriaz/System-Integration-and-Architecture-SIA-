def main():
    while True:
        print("\n" + "-" * 40)


        Name = input("Enter student name: ")
        grades_math = float(input("Enter Math grade: "))
        grades_english = float(input("Enter English grade: "))
        grades_science = float(input("Enter Science grade: "))

        # calculating the average of every subject
        Average = (grades_math + grades_english + grades_science) / 3

        # Displaying the output
        print("\n" + "=" * 40)
        print(f"Student: {Name}")
        print(f"Math = {grades_math}")
        print(f"English = {grades_english}")
        print(f"Science = {grades_science}")
        print(f"Average = {Average:.2f}")
        print("=" * 40)


        cont = input("\nAdd another student? (Y/N): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
