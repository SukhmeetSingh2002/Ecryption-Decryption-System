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

def TakeFileInput(inputFilePath):
    with open(inputFilePath, "r") as inputDataFile:
        dataAsString=inputDataFile.read()
        dataAsString=dataAsString.replace("\n","__________")
        dataAsString=dataAsString.replace(".", "0_00_0_0_0")
        dataAsString=dataAsString.replace(",", "7__77_7_77")
        dataAsList=splitData(dataAsString)
        dataAsList=[convertWordToBinary(x) for x in dataAsList]
    with open("my_file.txt", "w") as inputDataFile:
        inputDataFile.write(str(len(dataAsList)))
        inputDataFile.write("\n")
        for x in dataAsList:
            inputDataFile.write(f"0\n{x}\n")

def TakeFileInputDec(inputFilePath):
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

def OutputFile(TypeOfOp,outFileName):
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
            with open(outFileName, "w") as fout:
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
                newc.append(c[x])
            with open(outFileName, "w") as fout:
                for x in range(len(newc)):
                    fout.write(newc[x])
            ans=""
            with open(outFileName, "r") as fout:
                ans=fout.read()
            ans=ans.replace("__________","\n")
            ans=ans.replace("0_00_0_0_0",".")
            ans=ans.replace("7__77_7_77",",")
            with open(outFileName, "w") as fout:
                fout.write(ans)

def out_tex():
    with open("out_file.txt", "r") as file:
        with open("my_file.txt", "r") as y:
            n=int(y.readline())
            for i in range(n):
                w=int(y.readline())
                if w == 0:
                    u=y.readline()
                    i=file.readline()
                    c=""
                    k=""
                    for j in range(13):
                        c=c+converted(int(i[6*j:6*j+6],2))
                    for j in range(10):
                        k=k+converted(int(u[6*j:6*j+6],2))
                    print(f"\nYour message : \"{k}\" was encrypted as: \"{c}\"")
                elif w == 1:
                    u=y.readline()
                    i=file.readline()
                    c=""
                    k=""
                    for j in range(10):
                        c=c+converted(int(i[6*j:6*j+6],2))
                    for j in range(13):
                        k=k+converted(int(u[6*j:6*j+6],2))
                    print(f"\nYour message : \"{k}\" was decrypted as:  \"{c}\"")
                elif w == 2:
                    i=file.readline()
                    c=""
                    for j in range(10):
                        c=c+converted(int(i[6*j:6*j+6],2))
                    print(f"\nA random passowrd generated is : \"{c}\"")


print("Welcome")
print("Encrypt file takes input file and encrypts it and genrates .txt which conmtains encrypted data.")
print("Decrypt file takes previously encrypted file and decrypts it and generates a .txt file")
print("encrypt file currently supports following characters")
print(r"     1) numbers (0-9)")
print(r"     2) alphabets (a-z , A-Z)")
print(r"     3) characters ('\n', ' ', '_', ',', '.')")
print("Encrypting a message supports input of length of 10 characters containing alphanumeric and _")
print("Decrypting a message decrypts a previously encrypted message ")
print("Random password generator generates password of 10 characters consists alpha numeric characters and _ and spaces")
TypeOfOperation=int(input("Menu:\n1: Encrypt file\n2: Decrypt file\n3: Encrypt/Decrypt a message and generate random passwords of length upto 10\nPlease pick your choice: "))
if(TypeOfOperation==1):
    inputFilePath=input("Enter path of file to be encrypted: ")
    outFilePath=input("Enter path of file to store encrypted data: ")
    TakeFileInput(inputFilePath)
    os.popen("vvp.exe a.out")
    time.sleep(1)
    OutputFile(0,outFilePath)
    print(f"Your file \"{inputFilePath}\" was encrypted successfully and encrypted data is stored in \"{outFilePath}\"")
elif(TypeOfOperation==2):
    inputFilePath=input("Enter path of file to be decrypted: ")
    outFilePath=input("Enter path of file to store decrypted data: ")
    TakeFileInputDec(inputFilePath)
    os.popen("vvp.exe a.out")
    time.sleep(1)
    OutputFile(1,outFilePath)
    print(f"Your file \"{inputFilePath}\" was decrypted successfully and decrypted data is stored in \"{outFilePath}\"")
elif(TypeOfOperation==3):
    numOfOp=int(input("Enter number of operations: "))
    if(numOfOp>0):
        with open("my_file.txt", "w") as file:
            file.write(str(numOfOp))
            file.write("\n")
            for i in range(numOfOp):
                t=int(input("Select from following options:\n1: encrypt your message.(upto 10 characters)\n2: Decrypt a encrypted message.\n3: Generate a password\nSelect your choice:  "))
                file.write(f"{t-1}\n")
                if(t==1):
                    t=input("Enter your message to be encrypted: ")
                    r=""
                    for x in t:
                        r=r+convert(x)
                    r="0"*(60-len(r))+r
                    file.write(r)
                    file.write("\n")
                if(t==2):
                    t=input("Enter a encrypted message to be decrypted: ")
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

os.remove("my_file.txt")
os.remove("out_file.txt")