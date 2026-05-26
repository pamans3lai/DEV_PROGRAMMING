num1, num2 = 0, 1
print("Fibonacci series:")

for i in range(15):
    print(num1, end=" ")
    
    # calculate next term 
    res = num1 + num2

    # update values for next iteration
    #
    num1 = num2
    num2 = res
