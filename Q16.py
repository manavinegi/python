import pickle

#(i)
def add_record(filename):
    with open(filename, 'ab') as file:
        book_no = int(input("Enter Book Number: "))
        book_name = input("Enter Book Name: ")
        author = input("Enter Author's Name: ")
        price = float(input("Enter Price: "))
        record = {'Bookno': book_no, 'Bookname': book_name, 'Author': author, 'Price': price}
        pickle.dump(record, file)
        print("Record added successfully!")

#(ii)
def update_price(filename):
    updated = False
    temp_records = []

    with open(filename, 'rb') as file:
        try:
            while True:
                record = pickle.load(file)
                if record['Bookno'] == int(input("Enter Book Number to Update Price: ")):
                    record['Price'] = float(input("Enter New Price: "))
                    print("Price updated successfully!")
                    updated = True
                temp_records.append(record)
        except EOFError:
            pass
    #(iii)
    with open(filename, 'wb') as file:
        for record in temp_records:
            pickle.dump(record, file)
    
    if not updated:
        print("Book number not found!")

# Main menu
filename = 'Book.dat'

while True:
    print("\n--- Menu ---")
    print("a) Add Record")
    print("b) Update Price")
    print("c) Exit")

    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        add_record(filename)
    elif choice == 'b':
        update_price(filename)
    elif choice == 'c':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
