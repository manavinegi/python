def blank(f):
    f1=open(f,'r')
    x=0
    s=f1.read()
    for i in s:
        if i==' ':
            x+=1
    print("no of blanks:",x)

def line(f):
    f1=open(f,'r')
    x=0
    s=f1.readlines()
    for i in s:
        x+=1
    print("no of lines:",x)

def capital(f):
    f1=open(f,'r')
    x=0
    s=f1.read()
    for i in s:
        if i.isupper():
            x+=1
    print("no of capital alphabets:",x)

def small(f):
    f1=open(f,'r')
    x=0
    s=f1.read()
    for i in s:
        if i.islower():
            x+=1
    print("no of small alphabets:",x)

def vowel(f):
    f1=open(f,'r')
    x=0
    l=['a','e','i','o','u','A','E','I','O','U']
    s=f1.read()
    for i in s:
        if i in l:
            x+=1
    print("no of vowels:",x)

def capital_line(f):
    f1=open(f,'r')
    x=0
    for line in f1:
        if line[0].isupper():
            x+=1
    print("no of capital lines:",x)

def word(f):
    f1=open(f,'r')
    x=0
    for line in f1:
        for word in line.split():
            x+=1
    print("no of words:",x)

def digit(f):
    f1=open(f,'r')
    x=0
    s=f1.read()
    for i in s:
        if i.isdigit():
            x+=1
    print("no of digits:",x)

def upper(f):
    f1=open(f,'r')
    s=f1.read()
    st=s.upper()
    print(st)

def rev(f):
    f1=open(f,'r')
    s=f1.readline()
    while s:
        print(s[::-1])
        s=f1.readline()


f=input("file name with extension: ")

print()
print("a) Number of blanks present in the file.\nb) Number of lines present in the file.\nc) Number of capital alphabets present in the file.")
print("d) Number of small alphabets present in the file.\ne) Number of vowels present in the file.\nf) Number of lines starting with capital alphabets")
print('''g) Number of words present in the file.\nh) Number of digits present in the files.\ni) Content of file in Upper case.\nj) Content in Reverse case\n''')
c='y'
while c=='y':
    
    cho=int(input("choice (1/2/3..../10): "))

    if cho==1:
        blank(f)
    elif cho==2:
        line(f)
    elif cho==3:
        capital(f)    
    elif cho==4:
        small(f)
    elif cho==5:
        vowel(f)
    elif cho==6:
        capital_line(f)
    elif cho==7:
        word(f)    
    elif cho==8:
        digit(f)
    elif cho==9:
        upper(f)
    elif cho==10:
        rev(f)    
    else:
        print('invalid entry')
    c=input("y/n: ")
    print()
