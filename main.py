# pls run with an interpreter
# /bin/python3 ./main.py

from logic.operations import *

def main():
    print('Welcome to FAVE calculator!!')
    print("\n \n")
    print("*** What method you like to use? *** \n+ = (Addition) \n- = (Subtraction) \n% = (Modulos) \n/ = (Division) \n* = (Multiplication)"  "\n")
    method = input()
    print('What are the value you want to calculate?')
    a = int(input())
    b = int(input())
    calculate(method, a, b)
    
    
main()