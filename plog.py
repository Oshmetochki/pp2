def is_valid_password(p):
    
    def is_palindrome(a):
        a = [i.lower() for i in a if i not in (',.!?- ')]
        return a == a[::-1]
    def is_prime(b):
        return len([i for i in range(1, b+1) if b % i == 0]) == 2

        
    def even_or_odd(c):
        return c % 2 == 0
    def bolshe(k):
        return len(p)<=3 
    return is_prime(a) and is_palindrome(b) and even_or_odd(c) and bolshe(k)
p=input().split(':')   

a = p[0] ; b = int(p[1]); c = int(p[2]); k=len(p)
print(is_valid_password(p))
       

