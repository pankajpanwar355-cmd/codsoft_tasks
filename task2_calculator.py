def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("========== SIMPLE CALCULATOR ==========")
    print("Operations: +  -  *  /")

    while True:
        first = get_number("\nEnter the first number: ")
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second = get_number("Enter the second number: ")

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = first / second
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        print(f"Result: {first:g} {operator} {second:g} = {result:g}")

        again = input("Do another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Calculator closed.")
            break


if __name__ == "__main__":
    main()
