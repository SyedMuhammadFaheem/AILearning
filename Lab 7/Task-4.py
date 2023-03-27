from collections import OrderedDict
check=False
def getChar(unique,index):
    i=0
    for key in unique.keys():
        if i==index:
            return key
        i+=1

def getVal(word,unique):
    result=0
    for letter in word:
        if result==0 and unique[letter]==0:
            break
        result=(result*10)+unique[letter]
    return result

def cryptArithmetic(unique,numUsed,index,s1,s2,s3):
    global check
    if index==len(unique):
        n1=getVal(s1,unique)
        n2=getVal(s2,unique)
        n3=getVal(s3,unique)
        if (n1 or n2 or n3)==0:
            return
        if (n1+n2)==n3:
            print(n1,n2,n3)
            check=True
            unique=OrderedDict(sorted(unique.items()))
            for keys,values in unique.items():
                print(keys,values)
        return

    ch=getChar(unique,index)
    for i in range(10):
        if numUsed[i]==False:
            unique[ch]=i
            numUsed[i]=True
            cryptArithmetic(unique,numUsed,index+1,s1,s2,s3)
            if check:
                break
            numUsed[i]=False
            unique[ch]=-1


def cryptArithmeticSolve(s1,s2,s3):
    unique=dict()
    for letter in s1:
        if letter not in unique.keys():
            unique[letter]=-1
    for letter in s2:
        if letter not in unique.keys():
            unique[letter]=-1
    for letter in s3:
        if letter not in unique.keys():
            unique[letter]=-1
    numUsed=[False for i in range(10)]
    cryptArithmetic(unique,numUsed,0,s1,s2,s3)


cryptArithmeticSolve('CRACK','HACK','ERROR')
