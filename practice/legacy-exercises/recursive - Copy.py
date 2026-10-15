def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
n  = int(input("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
print(factorial_recursive(n))
