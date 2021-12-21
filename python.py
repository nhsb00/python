#sample # 1
for i in range(0,10):
    print (i, 2**i)

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
result = factorial(4)
print(result)