fo=open('file1.txt','r')
fi=open('file2.txt','w')
l=fo.readlines()
for i in l:
    if 'a' in i:
        i=i.replace('a','')
        fi.write(i)
fi.close()
fo.close()
