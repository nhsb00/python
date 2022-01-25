num = 3

if num % 2 == 0:
    result = "even number"
else:
    result = "odd number"

print(f'{num} is {result}')

number = 4
result = ('even number' if num % 2 == 0 else 'odd number')

print(f'{number} is {result}')

a_list = [1,3,2,5,1,2]

b_list = []

for a in a_list:
    b_list.append(a*2)

print(b_list)

b_list = [a*2 for a  in a_list]

print(b_list)



