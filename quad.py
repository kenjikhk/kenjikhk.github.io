import math 
  
  
def solve_quad( a, b, c): 
  
    d = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(d))
    x1 = ((-b + sqrt_val)/(2 * a))
    x2 = ((-b - sqrt_val)/(2 * a))
    x3 = (-b / (2 * a)) 

    if d > 0: 
        return (x1,x2)
    elif d == 0:  
        return x3     
    else:
        return None
  
