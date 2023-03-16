from random import *
from string import *

def generate_password(lenght):
    a = ''.join(set(ascii_uppercase)-set('lIoO'))
    a2 = ''.join(set(ascii_lowercase)-set('lIoO'))
    b=''.join(set(digits)- set('10'))
    c=[]
    for i in range(lenght):
        if len(c)//3==1:
            c.append((choice(b)))
        elif len(c)//2==1:
            c.append((choice(a2)))
        else:
            c.append(choice(a))
    return ''.join(c)

def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n,m)