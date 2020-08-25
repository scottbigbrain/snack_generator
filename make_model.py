import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec


sample = open("snacks.txt", "r")
s = sample.read() 



f = s.replace("\n", ". ") 
  
data = [] 

 
for i in sent_tokenize(f): 
	sentence = [] 
	   
	for j in word_tokenize(i): 
		sentence.append(j.lower()) 
  
	data.append(sentence) 
  

model = Word2Vec(data, min_count = 1, size = 60, window = 5, sg=1)
print("Model Made")
model.save("snacks.model")
print("Model Saved")
