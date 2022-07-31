import sys
sys.setrecursionlimit(10**6)

def factorial(n):
    if(n<0 or int(n)!=n):
        return "Not defined"
    elif(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number:"))
print("The factorial of given number=",factorial(n))
