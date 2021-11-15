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

x=int(input("Press 1 if you know number of operations to be done else press 2 if you dont know number of operations"))
if(x==1):
    try:
        q=int(input("Enter number of operations: "))
    except:
        q=-1
    if(q!=-1):
        with open("my_file.txt", "w") as file:
            file.write(q)
            file.write("\n")
            for i in range(q):
                t=input("Enter {}th password max characters = 10: ".format(i))
                r=""
                for x in t:
                    r=r+convert(x)
                r="0"*(60-len(r))+r
                file.write(r)
                file.write("\n")
elif(x==2):
    print("Enter any character to stop taking input")
else:
    print("Invalid Input")

    import os
    os.popen("vvp.exe a.out")
#OUTPUT
with open("out_file.txt", "r") as file:
    with open("my_file.txt", "r") as y:
        n=int(y.readline())
        n=int(y.readline())
        print(n)
        for i in range(n):
            w=int(y.readline())
            print(w)
            if w == 0:
                u=y.readline()
                i=file.readline()
                c=""
                k=""
                for j in range(12):
                    c=c+converted(int(i[6*j:6*j+6],2))
                for j in range(10):
                    k=k+converted(int(u[6*j:6*j+6],2))
                print(f"initial password {k} encrypted password {c}")
            elif w == 1:
                u=y.readline()
                i=file.readline()
                c=""
                k=""
                for j in range(10):
                    c=c+converted(int(i[6*j:6*j+6],2))
                for j in range(12):
                    k=k+converted(int(u[6*j:6*j+6],2))
                print(f"given password is {k} and its decrypted password is {c}")
            elif w == 2:
                i=file.readline()
                c=""
                for j in range(10):
                    c=c+converted(int(i[6*j:6*j+6],2))
                print(f"passowrd generated is : {c}")