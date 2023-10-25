age = -1
while age < 0 or age > 120:
    try:
        age = int(input("Enter your age (0-120): "))
        if age < 0 or age > 120:
        print("Invalid age. Please enter a value between 0 and 120.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


