#(i)
li=[]
a=int(input("NUMBER OF ELEMENTS IN THE LIST: "))
for i in range (a):
    s=int(input("Enter element: "))
    li.append(s)   
print()  
def one(li):
    for k in range (len(li)):
        if k%2==0:
            print(li[k],end=" ")
    print()
def two(li):
    l=[]
    for i in range(0,len(li)):
        if li[i]%2==0: 
            l.append(li[i])
    li=list(l)        
    print(li)


def three(li):
    ni=int(input("No of shifts= "))
    print("INITIAL LIST:",li)

    while ni>0:
        key=li[0]

        for i in range (1,len(li)):
            key,li[i]=li[i],key
        li[0]=key
        ni=ni-1
    print("REQUIRED LIST:",li)

def four(li):
    for i in range(len(li)):
        if li[i]%2==0:
            
           li[i]*=2
    print(li)

def five(li):
    n=len(li)
    for i in range(n):
        if i%2!=0:
            if li[i]%2==0:
                print(li[i])

def six(li):
    sum=0
    for i in range(len(li)):
        if li[i]%10==3:
            sum+=li[i]
    print(sum)

def seven(li):
    ide=int(input("index: "))
    ele=int(input("element: "))
    li.insert(ide,ele)
    print(li)

def eight(li):
    ele=int(input("element: "))
    li.append(ele)
    print(li)
    
print("1.PRINT ELEMENT AT EVEN INDEX\n2.REMOVE ODD NUMBERS FROM A LIST\n3.RIGHT CIRCULAR SHIFT ON LIST\n4.DOUBLR EVEN ELEMENT\n5.DISPLAY EVEN ELEMENTS AT ODD LOCATION\n6.DISPLAY SUM OF ELEMENTS ENDING WITH 3\n7.ADD ELEMENT AT LOCATION GIVEN BY USER\n8.APPEND ELEMENT TO LIST\n9.EXIT\n")
while True:
    cho=int(input("enter choice: "))
    if cho==1:
        one(li)
    elif cho==2:
        two(li)
    elif cho==3:
        three(li)    
    elif cho==4:
        four(li)    
    elif cho==5:
        five(li)
    elif cho==6:
        six(li)
    elif cho==7:
        seven(li)
    elif cho==8:
        eight(li)
    elif cho==9:
        break    
    else:
        print("INVALID CHOICE")
    print()
    


    
        
    
        
        
    
    
    
