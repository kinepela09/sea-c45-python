def fibonacci(n):
    """Returns the nth number from the Fibonacci sequence.

       Example: fibonacci(0) == 0
                fibonacci(1) == 1
    """

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """Returns the nth number from the Lucas series.

       Example: lucas(0) == 2
                lucas(1) == 1
    """

    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, zeroth, oneth):
    """Returns the nth number in a sequence with
        zeroth - an integer
        oneth - an integer

       Example: sum_series(0) == 0
                sum_series(1) == 1
                ...
                sum_series(n) ==sum_series(n-1) + sum_series(n-2)
    """

    if (n == 0):
        return zeroth
    elif (n == 1):
        return oneth
    else:
        return sum_series(n - 1, zeroth, oneth) + \
            sum_series(n - 2, zeroth, oneth)
