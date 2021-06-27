def big_fibo(n):
    if n <= 1:
       return n
    a = 1
    b = 0
    c = 0
    while len(str(a)) != n:
        c = b 
        b = a
        a = b + c 
    print (a)


