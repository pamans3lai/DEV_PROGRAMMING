def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a 
        a, b = b, a + b
        count += 1


fib = fibonacci_gen(8) 
print("First 8 Fibonacci numbers")
for num in fib:
    print(num, end= " ")
