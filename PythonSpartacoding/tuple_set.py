#tuple 'tuple' object does not support item assignment

# a = ('apple', 'pear', 'grape')

# a[1] = 'watermelon'

# print(a)

#set

# a=[1,2,3,4,5,1,2,3,4,5]

# a_set = set(a)
# print(a_set)

# a=['apple', 'pear', 'grape', 'strawberry']
# b=['apple', 'pear', 'grape', 'watermelon']

# a_set = set(a)
# b_set = set(b)

# print(a_set & b_set) #교집합
# print(a_set | b_set) #합집합

student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

a_set = set(student_a)
b_set = set(student_b)

print(a_set - b_set) #차집합
