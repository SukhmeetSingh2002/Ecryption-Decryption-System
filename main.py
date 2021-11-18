import os
import time

os.popen("iverilog.exe TestBench.v")
time.sleep(1)

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
def convertWordToBinary(word,lenWord=60):
    binWord=""
    for x in word:
        binWord=binWord+convert(x)
    binWord=binWord+"0"*(lenWord-len(binWord))
    return binWord

def splitData(dataString,lenWord=10):
    dataAsList = []
    while dataString:
        x=dataString[:lenWord]
        dataAsList.append(x)
        dataString=dataString[lenWord:]
    return dataAsList

def TakeFileInput():
    inputFilePath=input("Enter input file path: ")
    with open(inputFilePath, "r") as inputDataFile:
        dataAsString=inputDataFile.read()
        dataAsString=dataAsString.replace("\n","__________")
        dataAsString=dataAsString.replace(".", "_________")
        dataAsString=dataAsString.replace(",", "________")
        dataAsList=splitData(dataAsString)
        dataAsList=[convertWordToBinary(x) for x in dataAsList]
    with open("my_file.txt", "w") as inputDataFile:
        inputDataFile.write(str(len(dataAsList)))
        inputDataFile.write("\n")
        for x in dataAsList:
            inputDataFile.write(f"0\n{x}\n")

def TakeFileInputDec():
    inputFilePath=input("Enter path of file to be decrypted")
    with open(inputFilePath, "r") as inputDataFile:
        dataAsList = []
        dataAsString=inputDataFile.read()
        dataAsString=dataAsString.replace("\n","")
        dataAsString=dataAsString.replace(".", "")
        dataAsString=dataAsString.replace(",", "")
        dataAsList=splitData(dataAsString,13);
        dataAsList=[convertWordToBinary(x,78) for x in dataAsList]
    with open("my_file.txt", "w") as inputDataFile:
        inputDataFile.write(str(len(dataAsList)))
        inputDataFile.write("\n")
        for x in dataAsList:
            inputDataFile.write(f"1\n{x}\n")

def OutputFile(TypeOfOp):
    with open("out_file.txt", "r") as f:
        dataAsBinary=f.readlines()
        c=[]
        if TypeOfOp==0:
            for i in dataAsBinary:
                if i!='\n':
                    for j in range(13):
                        c.append((converted(int(i[6*j:6*j+6],2))))
                else:
                    c=c+list("\n")
            with open("new.txt", "w") as fout:
                fout.writelines(c)

        elif TypeOfOp==1:
            c=[]
            for i in dataAsBinary:
                if i!='\n':
                    for j in range(10):
                        c=c+list(converted(int(i[6*j:6*j+6],2)))
                else:
                    c=c+list("\n")
            newc=[]
            for x in range(len(c)):
                if x>0 and c[x]==' ' and c[x-1]==' ':
                    pass
                else:
                    newc.append(c[x])
            with open("new.txt", "w") as fout:
                for x in range(len(newc)):
                    fout.write(newc[x])
            ans=""
            with open("new.txt", "r") as fout:
                ans=fout.read()
            ans.replace("__________","\n")
            ans.replace("_________",".")
            ans.replace("________",",")
            with open("new.txt", "w") as fout:
                fout.write(ans)

def out_tex():
    with open("out_file.txt", "r") as file:
        with open("my_file.txt", "r") as y:
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
                    for j in range(13):
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
                    for j in range(13):
                        k=k+converted(int(u[6*j:6*j+6],2))
                    print(f"given password is {k} and its decrypted password is {c}")
                elif w == 2:
                    i=file.readline()
                    c=""
                    for j in range(10):
                        c=c+converted(int(i[6*j:6*j+6],2))
                    print(f"passowrd generated is : {c}")

x=int(input("Welcome\nMenu:\n1: Encrypt file\n2: Decrypt file\n3: Encrypt/Decrypt some passwords and generate some passwords of length upto 10"))
if(x==1):
    TakeFileInput()
    os.popen("vvp.exe a.out")
    time.sleep(1)
    OutputFile(0)
elif(x==2):
    TakeFileInputDec()
    os.popen("vvp.exe a.out")
    time.sleep(1)
    OutputFile(1)
elif(x==3):
    try:
        q=int(input("Enter number of operations: "))
    except:
        q=-1
    if(q!=-1):
        with open("my_file.txt", "w") as file:
            file.write(str(q))
            file.write("\n")
            for i in range(q):
                t=int(input("Select from following options:\n1: encrypt your password.(upto 10 characters)\n2: Decrypt your encrypted password.\n3: Generate a password "))
                file.write(f"{t-1}\n")
                if(t==1):
                    t=input("Enter your password: ")
                    r=""
                    for x in t:
                        r=r+convert(x)
                    r="0"*(60-len(r))+r
                    file.write(r)
                    file.write("\n")
                if(t==2):
                    t=input("Enter your password: ")
                    r=""
                    for x in t:
                        r=r+convert(x)
                    r="0"*(60-len(r))+r
                    file.write(r)
                    file.write("\n")    
        os.popen("vvp.exe a.out")
        time.sleep(1)
        out_tex()
else:
    print("Invalid Input")