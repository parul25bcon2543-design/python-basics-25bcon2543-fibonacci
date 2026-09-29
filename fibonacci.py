def fibonacci(n):
    # Initialize first two terms
    a, b = 0, 1
    # Check if number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
        return
    elif n == 1:
        print("Fibonacci sequence up to", n, "term:")
        print(a)
        return
    
    # Print the first n terms of Fibonacci sequence
    print("Fibonacci sequence up to", n, "terms:")
    for i in range(n):
        print(a, end=" ")
        # Calculate the next term
        a, b = b, a + b

# Get input from user
n = int(input("Enter the number of terms: "))
fibonacci(n)