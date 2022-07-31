def fibonacci(n):
    if (n<0 or int(n)!=n):
        return "Not defined"
    elif n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input('Enther the number:\n'))
print("The fibonacci series",end=" ")
for i in range(0,n):
    print(fibonacci(i),end=" ")