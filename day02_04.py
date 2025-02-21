# Assignment Day 02
# v1.3) Rewrite the code using the power function instead of the ** operator.
# v1.4) Make my_pow custom function instead of ** operator, power function and make it work.

def is_prime(num) -> bool:
    """
    A function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        #while i < (int(num ** 0.5) + 1):
        while i < (int(my_pow(num, 0.5)) + 1):
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

def my_pow(base, exp=2.0) -> float :
    return base ** exp
numbers = input("Input number : ").split()  # ex) 900 1000
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

j = n1
while j <= n2:
    if is_prime(j):
        print(j, end=' ')
    j = j + 1