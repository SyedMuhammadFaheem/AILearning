#Task 1
import nltk
from nltk.tokenize import sent_tokenize
text = "Joe waited for a train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station"
tokenizeSentences = sent_tokenize(text)
print(tokenizeSentences)