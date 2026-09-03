
def is_prime(n):
   
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def is_armstrong(n):

    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == n


def is_palindrome(n):
   
    text = str(n)
    return text == text[::-1]
