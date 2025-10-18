from src.utils import add, substract, multiply, divide


def _get_number(prompt):
    while True:
        raw = input(prompt)
        try:
            val = float(raw)
            return int(val) if val.is_integer() else val
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def _print_menu():
    print("Select one of the following operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


def main():
    while True:
        _print_menu()
        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        a = _get_number("Enter first number: ")
        b = _get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = substract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)
            print(f"The result is: {result}")
        except ValueError as exc:
            print(f"Error: {exc}")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
