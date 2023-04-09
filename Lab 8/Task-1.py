import random
def calculateProb(sample):
    tempScore=0   
    for i in range(sample):
        dieOne=random.randint(1,6)
        dieTwo=random.randint(1,6)
        score=dieOne+dieTwo
        if score%2==0 or score>7:
            tempScore+=1
    score=tempScore/sample
    print('The Probability Percentage is:',score*100)

def generateSample():
    sample=int(random.random()*100000)
    return sample
calculateProb(generateSample())