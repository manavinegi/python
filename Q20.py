#stack implementation
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
#main
stack=[]
top=None
while True:
    print("stack operations")
    print("1.Push")
    print("2.POP")
    print("3.Display")
    print("4.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        item=int(input("enter item:"))
        Push(stack,item)
        print(stack)
    elif ch==2:
        item=Pop(stack)
        if item=="Underflow":
            print("underflow!stack is empty")
        else:
            print("popped item is",item)
            print(stack)
    elif ch==3:
        print(stack)
    elif ch==4:
        break
    else:
        print("invalid choice!")
