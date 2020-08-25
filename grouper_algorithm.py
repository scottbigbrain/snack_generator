import random
import numpy as np

from custom_functions import *


class Grouper:

	def __init__(self, dataset, centroid_num, stop_at=0):
		self.stop_at = stop_at

		# we put dataset first so that the centroids can be near random dataset values
		self.dataset = dataset


		# average_set_len = int( len(self.dataset) / centroid_num )
		# self.centroid_sets = chunks(self.dataset, average_set_len)

		# holds the centroid sets, which hold all of the data_points associated with a particular centroid
		self.centroid_sets = []
		average_set_len = int( len(self.dataset) / centroid_num )

		avaliable_data_points = self.dataset.copy()
		for i in range(centroid_num):
			centroid_set = []

			# make sure we use all data_points
			if (i == centroid_num - 1):
				set_len = len(avaliable_data_points)
			else:
				set_len = average_set_len

			# fill a centroid_set and make sure that there are no repeats.
			for j in range(set_len):
				data_point = random.choice(avaliable_data_points)

				avaliable_data_points.remove(data_point)
				centroid_set.append(data_point)

			self.centroid_sets.append(centroid_set)


		# centroids start as the geometric mean of our centroid sets.
		self.centroids = []
		for c_set in self.centroid_sets:
			centroid_set = []
			for i in c_set:
				centroid_set.append(i.snack_vec)

			self.centroids.append(mean_coordinate(centroid_set))

		self.centroid_num = centroid_num

		# this is here so we can see what the previous centroids were. This way we can see if the centroids moved at all.
		self.previous_centroids = self.centroids
			

		# holds the label of each data_point in the dataset
		# self.data_labels = []

		# here the centroid sets change, so we will need to recalcalculate the centroids.
		# self.label_dataset()



	def label_dataset(self):

		#clear centroid_sets
		for centroid_set in self.centroid_sets:
			centroid_set.clear()

		# find closest centroid for each datapoint
		for data_point in self.dataset:

			closest_centroid = self.centroids[0]
			closest_dist = dist_between(data_point.snack_vec, self.centroids[0])
			closest_centroid_index = 0

			for i in range(len(self.centroids)):

				dist_to_centroid = dist_between(data_point.snack_vec, self.centroids[i])

				if (dist_to_centroid < closest_dist):
					closest_centroid = self.centroids[i]
					closest_dist = dist_to_centroid
					closest_centroid_index = i

			# label the data_point and put it in the associated centroid set
			# self.data_labels.append(closest_centroid_index)
			self.centroid_sets[closest_centroid_index].append(data_point)



	def execute_algorithm(self):
		# we label dataset before and after to constantly update centroid sets to remove errors
		# where we think that we are done but arent


		self.label_dataset()

		self.previous_centroids = self.centroids

		for i in range(len(self.centroids)):
			centroid_set = []
			for j in self.centroid_sets[i]:
				centroid_set.append(j.snack_vec)

			# print(dist_between( self.centroids[i], mean_coordinate(centroid_set) ))


			set_mean = mean_coordinate(centroid_set)

			self.centroids[i] = set_mean

		self.label_dataset()


		if (self.check_if_done() == True):
			print("Training Complete")
			return "Training complete"
		else:
			return "Training incomplete"


	def check_if_done(self):

		# find the distances between the centroids and the previous centroids

		distances = []
		for i in range(len(self.centroids)):
			d = dist_between(self.centroids[i], self.previous_centroids[i])
			distances.append(d)

		# print(distances)


		# find the highest value in distances

		highest_dist = distances[0]
		for dist in distances:
			if (dist > highest_dist):
				dist = highest_dist


		# if the highest dist is less than our stop at than that means we can stop training

		if (highest_dist <= self.stop_at):
			return True


