


stack=[]

while (a := input()) != 'close':
    if a.split()[0] == 'add':
        stack.append(a.split()[1])

    elif a == 'pop':
        print(stack.pop(-1))
    elif a == 'head':
        print(stack[-1])


