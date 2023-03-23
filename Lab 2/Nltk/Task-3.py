#Task 3
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
text = "Joe waited for a train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station"
tokenizeSentences = sent_tokenize(text)
for i in range(len(tokenizeSentences)):
    tokenizeSentences[i] = word_tokenize(tokenizeSentences[i])
print(tokenizeSentences)