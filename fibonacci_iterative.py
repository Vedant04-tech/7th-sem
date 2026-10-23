"""Print the first n Fibonacci numbers using a loop."""

n = int(input("Enter number of terms: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    a, b = 0, 1
    print("Fibonacci series:", end=" ")

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()
