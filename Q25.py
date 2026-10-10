import mysql.connector
con=mysql.connector.connect(host="localhost",password="123456",user="root",database="Bresult")
cur=con.cursor()
if (con.is_connected()==True):
    print("Connection Established")
    cur.execute("create table IF NOT EXISTS Board_Result (Adno varchar(50),Name varchar(30),stream varchar(20),Percentage decimal(5,2))")
    print("1.Add New Student\n2.Count of students streamwise.\n3.Select the school topper\n4.Select toppers stream wise\n5.Select lowest marks stream wise\n6.Display records of students having distinction.\n7.Display students scoring more than 90%.")
    while True:
        ch=int(input("Enter your choice-->"))
        if (ch==1):
            while True:
                adno=input("Admission no-->")
                name=input("Name-->")
                stream=input("Stream-->")
                per=float(input("Percentage-->"))
                query="Insert into Board_Result values('{}','{}','{}',{})".format(adno,name,stream,per)
                cur.execute(query)
                con.commit()
                print("ROW INSERTED")
                w=input("Do you wish to continue adding a record(Y/N)")
                if (w=="n" or w=='N'):
                    break
        elif (ch==2):
            cur.execute("select stream,count(*) from Board_Result group by stream")
            data=cur.fetchall()
            print("Stream Wise Count of Students->")
            for i in data:
                print(i)
        elif (ch==3):
            cur.execute("select adno,name,stream,max(percentage) from board_result")
            data=cur.fetchall()
            print("Details of School Topper->")
            for i in data:
                print(i)
        elif (ch==4):
            cur.execute("select max(percentage),stream from Board_result group by stream")
            data=cur.fetchall()
            print("Stream Wise Toppers->") 
            for i in data:
                print(i)
        elif (ch==5):
            cur.execute("select min(percentage),stream from Board_result group by stream")
            data=cur.fetchall()
            print("Stream Wise Lowest Marks->")
            for i in data:
                print(i) 
        elif (ch==6):
            cur.execute("select * from board_result where percentage>=75")
            data=cur.fetchall()
            print("ABOVE 75")
            for i in data:
                print(i)
        elif (ch==7):
            cur.execute("select * from board_result where percentage>=90")
            data=cur.fetchall()
            print("ABOVE 90")
            for i in data:
                print(i)
