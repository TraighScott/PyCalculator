import add
import multiply
import subtract
import divide

def main():
    try:
        operation = int(input("Select an operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"))
    except ValueError:
        print("ERROR: Please enter a valid input")
        return

    if operation not in [1, 2, 3, 4]:
        print("ERROR: Please enter a valid operation")
        return

    n1 = int(input("First number to be calculated: "))
    n2 = int(input("Second number to be calculated: "))

    if operation == 1:
        print(n1, "+", n2, "=", add.add(n1,n2))
    elif operation == 2:
        print(n1, "-", n2, "=", subtract.subtract(n1,n2))
    elif operation == 3:
        print(n1, "*", n2, "=", multiply.multiply(n1,n2))
    elif operation == 4:
        print(n1, "/", n2, "=", divide.divide(n1,n2))

if __name__ == "__main__":
    main()