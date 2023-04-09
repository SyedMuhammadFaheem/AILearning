import math
def nCr(n,r):
    f = math.factorial
    return f(n)//f(r)//f(n-r)

#Part a 
totalSampleCombination=nCr(60,5)
whiteBalls=nCr(10,3)
redBalls=nCr(20,2)
probPercentage=(whiteBalls+redBalls)/totalSampleCombination
print('Part A Probability Percentage:',probPercentage*100)

#Part b
whiteBalls=nCr(10,5)/totalSampleCombination
redBalls=nCr(20,5)/totalSampleCombination
greenBalls=nCr(30,5)/totalSampleCombination
probPercentage=(whiteBalls+redBalls+greenBalls)
print('Part B Probability Percentage:',probPercentage*100)