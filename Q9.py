T=()
nu=int(input("number of elements in Tuple: "))
for j in range (nu):
    a=int(input("enter element: "))
    T=T+(a,)   

dict={}
for k in T:
        if k in dict:
            dict[k]+=1
        else:
            dict[k]=1
            
print(dict) 
    

   


