def half(my_list):
    if len(my_list)%2 == 0:
        start = 0
    else:
        start = 1
        
    L = len(my_list)//2
    
    for i in range(L):
        temp = my_list[i]
        my_list[i] = my_list[i+L+start]
        my_list[i+L+start] = temp

my_list =eval(input("Enter a list: "))
half(my_list)
print(my_list)
