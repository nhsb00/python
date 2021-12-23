#sample # 1
for i in range(0,10):
    print (i, 2**i)
#sample # 2
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
result = factorial(4)
print(result)

#sample 3
def validate(num):
    if (num < 1 or num > 9):
        print('Out of range')
    elif (num != int(num)):
        print('Not an integer')
    else:
        return True
    return False

print (validate(-5))
print (validate(15))
print (validate(-5.2))
print (validate(2))
