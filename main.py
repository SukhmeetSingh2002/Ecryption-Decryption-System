def convert(x):
    if(ord(x)>=65 and ord(x)<=90):
        z=ord(x)-65+1
    elif(ord(x)>=97 and ord(x)<=122):
        z=ord(x)-97+27
    elif(ord(x)==95):
        z=53
    elif(ord(x)>=48 and ord(x)<=57):
        z=ord(x)-48+54
    else:
        z=0
    return "{0:06b}".format(z)

def converted(x):
    if(x>=1 and x<=26):
        z=chr(x+65-1)
    elif(x>=27 and x<=52):
        z=chr(x+97-27)
    elif(x==53):
        z="_"
    elif(x>=54 and x<=63):
        z=chr(x+48-54)
    else:
        z=" "
    return z

try:
    q=int(input("Enter number of passwords: "))
except:
    q=-1
if(q!=-1):
    with open("input.list", "w") as file:
        for i in range(q):
            t=input("Enter {}th password max characters = 10: ".format(i))
            r=""
            for x in t:
                r=r+convert(x)
            r="0"*(60-len(r))+r
            file.write(r)
            file.write("\n")


import os
os.popen("vvp.exe a.out")

with open("output.list", "r") as file:
    q=file.readlines()
    print(type(q))
    for i in q:
        c=""
        for j in range(12):
            c=c+converted(int(i[6*j:6*j+6],2))
        print(c)