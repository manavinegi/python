def Palindrome():
    f=a[::-1]
    if a==f:
        print("The given string is a Palindrome")
    else:
        print("The given string is not a Palindrome")



def no_of_char():
    alphabets=0
    numbers=0
    uppercase=0
    lowercase=0
    space=0
    for i in a:
        if i.islower():
            lowercase+=1
        elif i.isupper():
            uppercase+=1
        elif i.isdigit():
            numbers+=1
        if i.isalpha():
            alphabets+=1
        
    print("The number of uppercase letters:",uppercase)
    print("The number of lowercase letters:",lowercase)
    print("The number of digitcase letters:",numbers)
    print("The number of alphabets letters:",alphabets)

print("1.PALINDROME\n2.STASTICS")
cho=int(input("your choice: "))
a=input("Enter a string: ")

if cho==1:
    Palindrome()
elif cho==2:
    no_of_char()
else:
    print("invalid entry")    
    
    
