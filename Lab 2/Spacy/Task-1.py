#Task 1
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
sentence= input("Enter the sentence: ")
doc = nlp(sentence)
displacy.serve(doc, style="dep",port=49329)