import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
pul="il1Lo0O"
chars = ''

n = int(input('Укажите количество паролей для генерации:'))
l = int(input('Укажите длину одного пароля:'))
digon = input('Включать ли цифры 0123456789? (y/n)')
big = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
symb = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
neod = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
a=0
while a!=n:
    while len(chars)!=l:
        if digon=='y':
            chars+=random.choice(digits)
            if len(chars)==l:
                print(chars)
                continue
        if big =='y':
            chars+=random.choice(uppercase_letters)
            if len(chars)==l:
                print(chars)
                continue
        if low=='y':
            chars+=random.choice(lowercase_letters)
            if len(chars)==l:
                print(chars)
                continue
        if symb=='y':
            chars+=random.choice(punctuation)
            if len(chars)==l:
                print(chars)
                continue
        if neod == "n":
            chars += random.choice(pul)
            if len(chars) == l:
                print(chars)
                continue
        if len(chars)<l:
            continue
    a+=1
    