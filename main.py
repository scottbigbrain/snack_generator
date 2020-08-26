import numpy as np
import json
import random
from custom_functions import *

from snack import Snack
from grouper_algorithm import Grouper

with open("grouper.json", "r") as f:
	global grouper_dict
	grouper_dict = json.load(f)

def dict_to_snack(snack_dict):
	snack_array = snack_dict["snack"]
	snack_word_lists = snack_dict["snack_word_vecs"]
	snack_word_vecs = []
	for value in snack_word_lists:
		snack_word_vecs.append(np.array(value))

	snack = Snack(snack_array, snack_word_vecs)
	return snack


stop_at = grouper_dict["stop_at"]
dataset_dict = grouper_dict["dataset"]
centroid_sets_list_form = grouper_dict["centroid_sets"]
centroids_list_form = grouper_dict["centroids"]

centroids = []
for list_form in centroids_list_form:
	centroids.append(np.array(list_form))

dataset = []
for snack_dict in dataset_dict:
	dataset.append(dict_to_snack(snack_dict))


centroid_sets = []
for dict_c_set in centroid_sets_list_form:
	c_set = []
	for snack_dict in dict_c_set:
		c_set.append(dict_to_snack(snack_dict))

	centroid_sets.append(c_set)

grouper = Grouper(dataset, len(centroids), stop_at)
grouper.centroids = centroids
grouper.centroid_sets = centroid_sets





set_scores = []
for i in range(len(grouper.centroid_sets)):
	set_scores.append([5])

average_ratings = []
for i in range(len(set_scores)):
	average_ratings.append(0)


def update_averages():
	for i in range(len(set_scores)):
		total = 0
	for j in range(len(set_scores[i])):
		total += set_scores[i][j]
		average_ratings[i] = total


rating_num = 10;

for i in range(rating_num):
	set_index = random.randint(0, len(grouper.centroid_sets) - 1)
	c_set = grouper.centroid_sets[set_index]

	snack = random.choice(c_set).snack_string
	input_rating = float( input("On a scale of 1 to 10, how would you rate " + snack + ".  Answer: ") )
	set_scores[set_index].append(input_rating)
	update_averages()






best_centroid_set = grouper.centroid_sets[0]
best_rating = average_ratings[0]
for i in range(1, len(grouper.centroid_sets)):
	if (average_ratings[i] > best_rating):
		best_rating = average_ratings[i]
		best_centroid_set = grouper.centroid_sets[i]


def make_new_snack_idea(snack_set):
	highest_snack_len = len(snack_set[0].snack)
	for i in range(1, len(snack_set)):
		snack_len = len(snack_set[i].snack)
		if (snack_len > highest_snack_len):
			highest_snack_len = snack_len

	snack_len = random.randint(1, highest_snack_len)

	snack_array = []
	for i in range(snack_len):
		base_snack = random.choice(snack_set).snack
		added_word = random.choice(base_snack)
		snack_array.append(added_word)

	snack_string = ""
	for i in range(len(snack_array)):
		snack_string += snack_array[i]
		if (i < len(snack_array) - 1):
			snack_string += ' '

	return snack_string


snack_idea = make_new_snack_idea(best_centroid_set)
print("You might like " + snack_idea + '.')
