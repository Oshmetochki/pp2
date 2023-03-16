import heapq
list=[int(i) for i in input().split()]
heapq.heapify(list)
while (n:=input())!='end':
    if n.split()[0]=='insert':
        heapq.heappush(list,int(n.split()[1]))
    elif n.split()[0]=='pop':
        list.sort()
        print(list.pop())


