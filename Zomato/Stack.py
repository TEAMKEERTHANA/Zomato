stack=[]
def push():
    if len(stack)==n:
        print("Stack is full")
    else:
        element=input("Enter the element:")
        stack.append(element)
        print(stack)
def dequeue():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)

n=int(input("Enter the stack limit:"))
while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the correct operation")
