def mask_check(mask):                   #Маску переводим в бинарное число + склеиваем в стр

    mask=[str(bin(i)) for i in mask]
    mask=[i.replace('0b','') for i in mask]
    list=[]
    for i in mask:

        if (a:=len(i))<8:
            a=8-a
            i='0'*a+i
        elif a>8:
            return False
        list.append(i)

    list=''.join(list)
    return chekkk(list)


def chekkk(string=str):
    a=0
    for i in range(len(string)-1):
        if string[i]<string[i+1]:
            a=1
    return a==0


def ip_check(ip):

    a = 0;
    b = 0
    if len(ip)<4:
        return False
    for i in ip:
        if 0 <= i <= 255:
            a += 1
    for i in range(3):
        if ip[i] == ip[i + 1]:
            b += 1
    return a == 4 and b < 3


ip=[int(i) for i in input().split('.')]
maska=[int(i) for i in input().split('.')]

if ip_check(ip) and mask_check(maska):
    a=[]
    for i in range(len(maska)):
        b=int(maska[i])
        c=int(ip[i])
        a.append(b&c)
    print(*a, sep='.')
else:
    print("Валидация не пройдена")














