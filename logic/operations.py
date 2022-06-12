
def calculate(method, a, b):
    print("====== solution ======")
    
    if method == "+":
        print(sum(a,b))
    elif method == "-":
        print(sub(a,b))
    elif method == "%":
        print(mod(a,b))
    elif method == "/":
        print(divide(a,b))
    elif method == "*":
        print(multi(a,b))



#multiplication
def multi(x, y):
    return x*y

#addition
def sum(x, y):
    return x+y

#ssubtraction
def sub(x, y):
    return x-y
  
#division
def divide(x,y):
    return x/y

#modulos
def mod(x, y):
    return x%y



