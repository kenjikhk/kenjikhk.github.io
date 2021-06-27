def is_prime(n):
    for i in range(2,n):
        if n <= 1:
            return False
        elif (n % i) == 0:
            return False
    return True


        
    