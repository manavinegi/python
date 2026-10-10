def displayMeMy():
    num=0
    f=open("story.txt",'r')
    N=f.read()
    M=N.split()
    for i in M:
        if i=="My" or i=="Me":
            print(i)
            num=num+1
    f.close()
    print("Count of Me/My if file",num)
displayMeMy()
