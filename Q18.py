import csv

def Add_detail(filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        print("Enter the details of the student:")
        sport_id = int(input("Sport ID: "))
        competition = input("Competition Name: ")
        prize_won = input("Prize Won (Gold/Silver/Bronze): ")

        writer.writerow([sport_id, competition, prize_won])
        print("Details added successfully!")

def Count_Medal(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  
        gold_competitions = []  
        
        for row in reader:
            if row[2].strip().lower() == 'gold':  
                competition = row[1]
                if competition not in gold_competitions: 
                    gold_competitions.append(competition)
        
        print("Competitions where students won Gold medals:")
        for competition in gold_competitions:
            print(competition)

filename = 'sports.csv'

while True:
    print("\n--- Menu ---")
    print("1. Add Student Detail")
    print("2. Display Competitions with Gold Medals")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        Add_detail(filename)
    elif choice == 2:
        Count_Medal(filename)
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
