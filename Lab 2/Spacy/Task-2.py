#Task 2
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
sentence= input("Enter the sentence: ")
doc = nlp(sentence)
doc=set(doc)
for token in doc:
    print(token,token.idx)