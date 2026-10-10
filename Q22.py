EvenNumbers = []

def push_even(N):
    """
    Push all even numbers from the list N into the EvenNumbers stack.
    """
    for num in N:
        if num % 2 == 0:
            EvenNumbers.append(num)


def pop_even():
    """
    Pop the topmost number from the EvenNumbers stack and return it.
    If the stack is empty, display 'Empty'.
    """
    if EvenNumbers:
        return EvenNumbers.pop()
    else:
        print("Empty")
        return None


def disp_even():
    """
    Display all elements of the EvenNumbers stack.
    If the stack is empty, display 'None'.
    """
    if EvenNumbers:
        print("Stack contents:", EvenNumbers)
    else:
        print("None")

print("Enter a list of integers (e.g., [10, 15, 20, 25, 30]):")
numbers = eval(input()) 

print("Pushing even numbers from the list:", numbers)
push_even(numbers)

while True:
    print("\n--- Stack Operations Menu ---")
    print("1. Display all even numbers in the stack")
    print("2. Pop the topmost even number")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("\nDisplaying the stack:")
        disp_even()
    elif choice == 2:
        print("\nPopping the topmost number:")
        print("Popped number:", pop_even())
    elif choice == 3:
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
