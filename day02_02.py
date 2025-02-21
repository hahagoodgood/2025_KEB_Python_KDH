# Assignment Day 02
# v1.1) Change the for phrase to the while phrase.
# v1.2) Write a program that receives two numbers and outputs only prime numbers between the two numbers. Then, use only the while statement and include the two numbers entered.
# v1.3) Rewrite the code using the power function instead of the ** operator.
# v1.4) Make my_pow custom function instead of ** operator, power function and make it work.
from altair import param


def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while i < (int(num ** 0.5) + 1):
        #for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

def find_primes(num_A, num_B) -> None :
    """
    A function that print prime number between the two number
    :param num_A: integer number
    :param num_B: integer number
    """
    prime_numbers = []
    for i in range(num_A, num_B + 1):
        if is_prime(i):
            prime_numbers.append(i)
    print(f"The prime numbers between A and B are {prime_numbers}")

# main
#help(abs)
#help(is_prime)
# n = int(input("Input number : "))
#
# if is_prime(n):  # function call
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is NOT prime number!")
help(find_primes)
a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))
find_primes(a,b)