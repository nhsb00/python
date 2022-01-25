def cal(a,b=2):
    return a+2*b

result = cal(1)
print(result)

def eat(*args):
    for name in args:
        print(f'{name} eat dinner')

eat('soo', 'bin')

def dic(**kwargs):
    print(kwargs)

dic(name='soo', age=2, height=180)