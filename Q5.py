#(i)
def lin_search(li,ele):
    n=len(li)
    for i in range(n):
        if li[i]==ele:
            print("element found at index:",i)
            break
        
    else:
        print("element not found")

#(ii)
def bin_search(li,ele):
    n=len(li)
    beg=0
    end=n-1

    while beg<=end:
        mid=(beg+end)//2
        if li[mid]==ele:
            print("element found at index",mid)
            break
        elif li[mid]>ele:
            end=mid-1
        elif li[mid]<ele:
            beg=beg+1

    else:
        print("element not found")
            
li=[]
nu=int(input("number of elements in list: "))
for j in range (nu):
    a=int(input("enter element: "))
    li.append(a)   



print("1.LINEAR SEARCH\n2.BINARY SEARCH")
cho=int(input("your choice: "))
ele=int(input("element to be found: "))

if cho==1:
    lin_search(li,ele)
elif cho==2:
    bin_search(li,ele)
else:
    print("invalid entry")
