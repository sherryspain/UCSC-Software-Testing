def factorial(x):
    i = x
    running_fact = 1
    while i > 0:
        running_fact *= i
        print running_fact
        i -= 1
    return running_fact
