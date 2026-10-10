import pickle
def add():
    f=open("sports.dat","ab")
    name=input("enter name: ")
    no=int(input("enter phone no: "))
    fee=int(input("enter fee: "))
    dic={'name':name,'phno':no,'fee':fee}
    pickle.dump(dic,f)
    f.close()

def search():
    f=open("sports.dat","rb")
    na=input("enter name: ")
    e=0
    try :
        while True:
            s=pickle.load(f)
            if s['name']==na:
                e=1
                print(s)
    except EOFError:
        f.close()
    if e==0:
        print("NO SUCH RECORD FOUND")

def delete():
    f1=open("sports.dat","rb")
    li=[]
    de=input("enter name to delete record: ")
    try :
        while True:
            s=pickle.load(f1)
            li.append(s)    
                    
    except EOFError:
        f1.close()
    
    f=open("sports.dat","w+b")
    for a in li:
        if a['name']!=de:
            pickle.dump(a,f)
    f.close()
def disp():
    f=open("sports.dat","rb")
    
    try :
        while True:
            s=pickle.load(f)
            print(s)
    except EOFError:
        f.close()
    
print("1.SEARCH RECORD\n2.APPEND NEW RECORD\n3.DELETE RECORD\n4.DISPLAY RECORDS\n5.EXIT")
while True:
    
    cho=int(input("choice= "))
    if cho==2:
        add()
    elif cho==1:
        search()
    elif cho==3:
        delete()
    elif cho==4:
        disp()
    elif cho==5:
        print("EXITED SUCCESSFULLY")
        break
    else:
        print("INVALID ENTRY")
    print()
