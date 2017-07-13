import random

def hello(name):
    print('Hello ' + name)
    print()


def get(num):
    if num < 1:
        return 'It is small.'
    elif num == 1:
        return str(num) + ' is ONE'
    elif num == 2:
        return str(num) + ' is TWO'
    elif num == 3:
        return str(num) + ' is THREE'
    else:
        return str(num) + ' is MUCH!'


hello('Alice')
hello('Bob')
for i in range(10):
    print(get(random.randint(0,5)))
