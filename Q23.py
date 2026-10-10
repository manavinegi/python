import mysql.connector
con=mysql.connector.connect(host="localhost",password="123456",user="root",database="employee_data")
cur=con.cursor()
if (con.is_connected()==True):
    print("connection established")
cur.execute("create table if not exists emp(empno int(10),name varchar(20), salary int(10))")
print("table-->emp,created successfully")
print("1.add record; 2.display all rec; 3.update salary using empno; 4.delete a record; 5.exit")
while True:
    ch=int(input("enter your choice"))
    if (ch==1):
        while True:
            empno=int(input("enter emp number"))
            name=input("enter the name of employee: ")
            s=int(input("enter the salary of the employee:"))
            query="insert into emp values({},'{}',{})".format(empno,name,s)
            cur.execute(query)
            con.commit()
            print("row inserted")
            w=input("do you wish to continue adding a record(yes or no)")
            if(w=="no"):
                break
    elif (ch==2):
        cur.execute("select * from emp")
        data=cur.fetchall()
        print("All Records: ")
        for i in data:
            print(i)
    elif (ch==3):
        empno=int(input("Enter the empno whose salary is to be updated: "))
        salary=int(input("Enter the updated salary: "))
        query="update emp set salary={} where empno={}".format(salary,empno)
        cur.execute(query)
        con.commit()
        print("SALARY UPDATED")
    elif (ch==4):
        empno=int(input("Enter empno whose rec is to be deleted: "))
        query="delete from emp where empno={}".format(empno)
        cur.execute(query)
        con.commit()
        print("RECORD DELETED")
    elif (ch==5):
        print("end of program")
        break
    else:
        print("INVALID CHOICE")
    
