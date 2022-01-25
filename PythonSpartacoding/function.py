#function 

# def hello():
#     print('Hello!')
#     print("Nice weather")

# hello()
# hello()


# def sum(a,b):
#     print('you add them up')
#     return a+b

# result = sum(1,2)
# print(result)

# def bus_rate(age):
#     if age >65:
#         print("it is free")
#         return 0
#     elif age > 20:
#         print("you are adult")
#         return 1200
#     else:
#         print("you are student")
#         return 750

# myrate = bus_rate(15)
# print(myrate)

def check_gender(ssn):
    gender = ssn.split('-')[1][0]
    if int(gender) == 1:
        print("male")
    elif int(gender) == 2:
        print("female")
    else:
        print("unknown")

check_gender('111111-1111111')
check_gender('111111-2111111')
check_gender('111111-4111111')