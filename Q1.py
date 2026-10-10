#(i)
import random
n=int(input("Enter the number of random numbers you have to generate: "))
a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))
def gen_ran_nos(n,a,b):
    return [random.randint(a, b) for i in range(n)]
i=(gen_ran_nos(n,a,b))

#(ii)
maximum=max(i)
minimum=min(i)

#(iii)
t=0
s=0
for k in i:
    if k%2==0:
        t+=1
    else:
        s+=1

#(iv)
average = sum(i) / len(i)

#Display
print(i)
print("The maximum value from the list is",maximum)
print("The minimum value from the list is",minimum)
print("The number of odd numbers is",s)
print("The number of even numbers is",t)
print("The average of all the numbers is",average)
            
    
        

