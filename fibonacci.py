def fib():
    prev = 1
    result = 1
    nth = 1
    nth = int(input("Enter the nth value for the Fibonacci number: "))
    for i in range(nth - 2):
       result, prev = prev+result, result
    print(result)
    fib()

fib()
