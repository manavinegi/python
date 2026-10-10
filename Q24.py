import mysql.connector
con=mysql.connector.connect(host="localhost",password="123456",user="root")
cur=con.cursor()
if (con.is_connected()==True):
      print("Connection Established")
cur.execute("create database if not exists sales")
cur.execute("use sales")
cur.execute("create table IF NOT EXISTS inventory (item varchar(50),cost int(10),quantity int(10))")
cur.execute("create table IF NOT EXISTS sales (Phone varchar(50),Item_Quan varchar(100),Cost int(10))")
print("1.Add Inventory\n2.Update Inventory\n3.Sale\n4.Sales Record\n5.EXIT")
while True:
      ch=int(input("Enter your choice-->"))
      if (ch==1):
             while True:
                   iname=input("Enter Item name-->")
                   cost=int(input("Enter Price per unit-->"))
                   quan=int(input("Enter Quantity-->"))
                   query="Insert into inventory values('{}',{},{})".format(iname,cost,quan)

                   cur.execute(query)
                   con.commit()# reflected in database
                   print("ROW INSERTED")
                   w=input("Do you wish to continue adding a record(yes or no)")
                   if (w=="no"):
                         break
         
      elif (ch==2):
         cur.execute("select * from inventory")
         data=cur.fetchall()
         print("All Records-->")
         for i in data:
            print(i)
         i_name=input("Enter item name to be updated-->")
         quan=int(input("Enter the fresh quantity->"))
         query="update inventory set quantity=quantity+{} where item='{}'".format(quan,i_name)
         cur.execute(query)
         con.commit()
         print("QUANTITY UPDATED")
      elif (ch==3):
         cur.execute("select * from inventory")
         data=cur.fetchall()
         print("All Records-->")
         for i in data:
            print(i)
         ch='y'
         n_bill=''
         bill_amount=0
         while True:
            n=input("Enter Product")
            q=int(input("Enter the quantity"))
            q1="Select quantity,cost from inventory where item='{}'".format(n)
            cur.execute(q1)
            data=cur.fetchall()
            p_quan=data[0][0]
            p_stock=data[0][1]
            if q>p_quan:
               print("Stock is not available")
            else:
               n_bill=n_bill+n
               print(n_bill)
               query="update inventory set quantity=quantity-{} where item='{}'".format(q,n)
               cur.execute(query)
               con.commit()
               bill_amount=bill_amount+(q*p_stock)
            opt=input("Do you want to add more items(y/n)")
            if opt=='n' or opt=='N':
               break
         b_choice=input("Do you wish to bill")
         if b_choice=='y':
            phone=input("Enter your phone no")
            query="Insert into sales values({},'{}',{})".format(phone,n_bill,bill_amount)
            cur.execute(query)
            con.commit()
            print("QUANTITY UPDATED")
      elif (ch==4):
         cur.execute("select * from sales")
         data=cur.fetchall()
         print("All Sales Records-->")
         for i in data:
            print(i)
      else:
         break
