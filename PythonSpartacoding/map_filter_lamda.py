import re


people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

def check_adult(person):
    if person['age'] > 20:
        return 'adult'
    else:
        return 'student'

def check_adult(person):
    return ('adult' if person['age'] > 20 else 'student')

result = map(check_adult, people)

result = map(lambda person: ('adult' if person['age'] > 20 else 'student'), people)

result = filter(lambda person: person['age'] > 20, people)
print(list(result))