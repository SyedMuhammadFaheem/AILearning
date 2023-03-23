#Task 7
str="Faheem1234"
countNum=0
countLetter=0
for i in range(len(str)):
    if ord(str[i])>=48 and ord(str[i])<=57:
        countNum+=1
    else:
        countLetter+=1
print(countLetter)
print(countNum)