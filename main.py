import os
import time

inputFilePath="my_file.txt"

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
    binWord="0"*(lenWord-len(binWord))+binWord
    return binWord

def splitData(dataString,lenWord=10):
    dataAsList = []
    while dataString:
        x=dataString[:lenWord]
        dataAsList.append(x)
        dataString=dataString[lenWord:]
    return dataAsList

def TakeFileInput(numOfOp):
    with open(inputFilePath, "r") as inputDataFile:
        dataAsList = []
        dataAsString=inputDataFile.read()
        dataAsList=splitData(dataAsString);
        for x in range(len(dataAsList)):
            if dataAsList[x]!='\n':
                dataAsList[x]=convertWordToBinary(dataAsList[x])

    with open("my_file.txt", "w") as inputDataFile:
        inputDataFile.write(str(numOfOp))
        inputDataFile.write("\n")
        inputDataFile.write("0")
        inputDataFile.write("\n")
        for x in dataAsList:
            inputDataFile.write(x)
            if '\n' not in x:
                inputDataFile.write('\n')

def TakeFileInputDec(numOfOp):
    with open(inputFilePath, "r") as inputDataFile:
        dataAsList = []
        dataAsString=inputDataFile.read()
        dataAsList=splitData(dataAsString,12);
        for x in range(len(dataAsList)):
            if dataAsList[x]!='\n':
                dataAsList[x]=convertWordToBinary(dataAsList[x],78)

    with open("my_file.txt", "w") as inputDataFile:
        inputDataFile.write(str(numOfOp))
        inputDataFile.write("\n")
        inputDataFile.write("1")
        inputDataFile.write("\n")
        for x in dataAsList:
            inputDataFile.write(x)
            if '\n' not in x:
                inputDataFile.write('\n')

def OutputFile():
    with open(inputFilePath, "r") as f:
        dataAsBinary=f.readlines()
        c=[]
        TypeOfOp=int(dataAsBinary[1])
        dataAsBinary=dataAsBinary[1:]
        dataAsBinary=dataAsBinary[1:]
        if TypeOfOp==0:
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
                fout.write("output\n")
                for x in range(len(newc)):
                    fout.write(newc[x])

        elif TypeOfOp==1:
            for i in dataAsBinary:
                if i!='\n':
                    for j in range(12):
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
                fout.write("output\n")
                for x in range(len(newc)):
                    fout.write(newc[x])
        elif TypeOfOp==2:
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
                fout.write("output\n")
                for x in range(len(newc)):
                    fout.write(newc[x])



x=int(input("Press 1 if you know number of operations to be done else press 2 if you dont know number of operations"))
if(x==1):
    TypeOfOp=int(input("Press 1 to encrypt file\n2 to decrypt file\n3 to generate password"))
    numberOfOp=int(input("Enter number of operations: "))
    if TypeOfOp==1:
        print("Enter the path of file to be enctrypted : ")
        TakeFileInput(numberOfOp)
    elif TypeOfOp==2:
        print("Enter the path of file to be dectrypted : ")
        TakeFileInputDec(numberOfOp)
    else:
        with open("my_file.txt", "w") as inputDataFile:
            inputDataFile.write(str(numberOfOp))
            inputDataFile.write("\n")
            inputDataFile.write("2")
            inputDataFile.write("\n")
elif(x==2):
    while(TypeOfOp<4):
        TypeOfOp=input("Press 1 to encrypt file\n2 to decrypt file\n3 to generate password\n4 to exit")
        if TypeOfOp==1:
            print("Enter the path of file to be enctrypted : ")
            TakeFileInput(1)
        elif TypeOfOp==2:
            print("Enter the path of file to be dectrypted : ")
            TakeFileInputDec(1)
        else:
            with open("my_file.txt", "w") as inputDataFile:
                inputDataFile.write(1)
                inputDataFile.write("\n")
                inputDataFile.write("2")
                inputDataFile.write("\n")
else:
    print("Invalid Input")

os.popen("vvp.exe a.out")

time.sleep(2)

OutputFile()