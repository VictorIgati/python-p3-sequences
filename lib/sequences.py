def print_fibonacci(length):
    """
    Prints the Fibonacci sequence up to the specified length.

    Parameters:
    length (int): The number of elements in the Fibonacci sequence to print.
    """
    fibonacci_sequence = []

    while len(fibonacci_sequence) < length:
        if len(fibonacci_sequence) == 0:
            fibonacci_sequence.append(0)
        elif len(fibonacci_sequence) == 1:
            fibonacci_sequence.append(1)
        else:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    print(fibonacci_sequence)
