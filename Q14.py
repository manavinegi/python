fo=open("hp.txt","w")
fo.write("Harry Potter")
fo.write("There is a difference in all harry potter books\nWe can see it as harry grows\nthe books were written by J.K rowling ")
fo.close()

fo=open('hp.txt','r')
fi=open('writehp.txt','w')
l=fo.readlines()
for i in l:
    if 'a' in i:
        i=i.replace('a','')
        fi.write(i)
fi.close()
fo.close()
