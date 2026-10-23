"""Print the first n Fibonacci numbers using recursion."""


def fibonacci(n):
    # Base cases stop the recursion.
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Each term is the sum of the previous two terms.
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter number of terms: "))

if terms < 0:
    print("Please enter a non-negative number.")
else:
    print("Fibonacci series:", end=" ")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
