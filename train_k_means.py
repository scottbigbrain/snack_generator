import numpy as np
import json
import time

from snack import Snack
from custom_functions import *
from grouper_algorithm import Grouper

from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec


model = Word2Vec.load("snacks.model")



sample = open("snacks.txt", "r")
s = sample.read() 

f = s.replace("\n", ". ") 
  
data = []
 
for i in sent_tokenize(f): 
	sentence = [] 
	
	for j in word_tokenize(i): 
		sentence.append(j.lower()) 

	data.append(sentence) 

snacks = []
for sentence in data:
	snack_word_vecs = []
	for i in range(len(sentence)):
			vec = model[ sentence[i] ]

			input_vec = []
			for value in vec:
				input_vec.append(float(value))

			snack_word_vecs.append(np.array(input_vec))

	snack = Snack(sentence, snack_word_vecs)
	snacks.append(snack)



grouping_dataset = []
for snack in snacks:
	grouping_dataset.append(snack)



grouper = Grouper(grouping_dataset, centroid_num=6, stop_at=0)

print("Training K Means")
training_state = grouper.execute_algorithm()
while (training_state == "Training Incomplete"):
	print("Training K Means")
	training_state = grouper.execute_algorithm()

# for snack in grouper.dataset:
# 	print(snack.snack)



dataset_dict = []
for i in grouper.dataset:
	dataset_dict.append(i.to_dict())

centroid_sets = []
for c_set in grouper.centroid_sets:
	centroid_set = []

	for data_point in c_set:
		centroid_set.append(data_point.to_dict())

	centroid_sets.append(centroid_set)

centroids = []
for centroid in grouper.centroids:
	centroids.append(list(centroid))


grouper_dict = {"stop_at": grouper.stop_at, "dataset": dataset_dict, "centroid_sets": centroid_sets, "centroids": centroids}

with open ("grouper.json", "w") as f:
	json.dump(grouper_dict, f)
	print("dumped")
