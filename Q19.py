import csv
def add():
    f=open("student.csv",'a')
    re=csv.writer(f)
    ano=int(input("enter ano: "))
    name=input("name: ")
    pc=int(input("enter percentage: "))
    li=[ano,name,pc]
    re.writerow(li)
    f.close()
    print("RECORD ADDED SUCCESSFULLY")
def search():
    f=open("student.csv",'r',newline='\n')
    an=int(input("enter ano to be searched: "))
    re=csv.reader(f)
    for i in re:
        if i[0]==str(an):
           print(i)           
def disp():
    f=open("student.csv",'r',newline='\n')
    re=csv.reader(f)
    print("[ANO , NAME , PERCENTAGE]")
    for i in re:
        print(i)
    f.close()

print("1.APPEND RECORD\n2.SEARCH RECORD\n3.DISPLAY RECORD\n4.EXIT\n")
while True:
    cho=int(input("choice: "))
    if cho==1:
        add()
    elif cho==2:
        search()
    elif cho==3:
        disp()
    elif cho==4:
        break           
    else:
        print("INVALID CHOICE")
    print()
