print('Welcome to FAVE calculator!!')
print("\n \n")
print("What method you like to use? \n+ = (Addition) \n- = (Subtraction) \n% = (Modulos) \n/ = (Division) \n* = (Multiplication)"  "\n")
method = input()
print('What are the value you want to calculate?')
a = int(input())
b = int(input())

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

   
