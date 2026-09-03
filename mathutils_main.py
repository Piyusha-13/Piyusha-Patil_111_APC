from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum


def main():
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    print("Addition:", add(first, second))
    print("Subtraction:", subtract(first, second))
    print("Multiplication:", multiply(first, second))
    if second != 0:
        print("Division:", divide(first, second))
    else:
        print("Division: not possible (division by zero)")

    number = int(input("\nEnter an integer to check: "))
    print("Prime:", is_prime(number))
    print("Armstrong:", is_armstrong(number))
    print("Palindrome:", is_palindrome(number))

    values = list(map(float, input("\nEnter numbers separated by spaces: ").split()))
    print("Mean:", mean(values))
    print("Maximum:", maximum(values))
    print("Minimum:", minimum(values))


if __name__ == "__main__":
    main()
