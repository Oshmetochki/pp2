def is_palindrome(a):    # Проверка на палиндром
    a = str(a)
    a = [i.lower() for i in a if i not in (',.!?- ')]
    return a == a[::-1]


def is_prime(b):    # Проверка на просто число
    b=int(b)
    return len([i for i in range(1, b + 1) if b % i == 0]) == 2


def even_number(c):         # Проверка четности
    return int(c) % 2 == 0

def is_valid_password(a,b,c):

    return is_palindrome(a) and is_prime(b) and even_number(c)

a=input().split(':')        # Проверка длинны
if len(a)>3:
    print('False')
elif len(a)==3:
    print(is_valid_password(a[0],a[1],a[2]))
















