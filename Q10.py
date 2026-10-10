def add(dictionary):
    country=input("Enter the country you want to add: ")
    capital=input("Enter the Capital of that country: ")
    dictionary[country]=capital
    
def disp(dictionary):
    for key in dictionary:
        print(key,'|',dictionary[key])
        
def search(dictionary):
    cou=input("Country to be searched: ")
    for key in dictionary:
        if key==cou:
            print("Country found")
            print(key,dictoinary[key])
            break
    else:
        print("Country not found")

def update(dictionary):
    cou=input("Country to be updated: ")
    nc=input("New capital")
    for key in dictionary:
        if key==cou:
            dictoinary[key]=nc
            
    

dictionary={}
n=int(input("No. of countries: "))

for i in range(n):
    country=input("Country: ")
    capital=input("Capital: ")
    dictionary[country]=capital
print()
print("1.ADD ENTRY\n2.DISPLAY\n3.SEARCH AND DISPLAY COUNTRY\n4.UPDATE CAPITAL\n5.EXIT\n")


while True:
    cho=int(input("Choice="))
    if cho==1:
        add(dictionary)
    elif cho==2:
        disp(dictionary)
    elif cho==3:
        search(dictionary)

    elif cho==4:
        update(dictionary)
    elif cho==5:
        break
    print()
