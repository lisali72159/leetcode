points = [ 2.0, 3.0, 7.0, 6.0 ]

def f(x):
    whole_num = int(x // 1)
    decimal = x % 1         
    
    start = points[(whole_num % 4)] 
    end = points[(whole_num + 1) % 4]
    return start - ((start - end) + decimal)


print f(1.6)
    