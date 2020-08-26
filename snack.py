import numpy as np

from custom_functions import *


class Snack:

	def __init__(self, snack_array, snack_word_vecs):
		self.snack = snack_array
		if (self.snack.count('.') > 0):
			periods = self.snack.count('.')
			for i in range(periods):
				self.snack.remove('.')
				
		self.snack_string = self.snack_to_string()

		# store the vector form of each word in self.snack
		self.snack_word_vecs = snack_word_vecs
		# for i in range(len(self.snack)):
		# 	vec = self.model[ self.snack[i] ]
		# 	self.snack_word_vecs.append(vec)


		self.snack_vec = mean_coordinate(self.snack_word_vecs)


	def snack_to_string(self):
		output = ''

		for i in range(len(self.snack)):
			output += self.snack[i]

			# dont add a space at the end
			if (i < len(self.snack) - 1):
				output += ' '

		return output


	def to_dict(self):

		snack_word_vecs = []
		for vec in self.snack_word_vecs:
			vec_list = list(vec)
			for i in vec_list:
				i = str(i)

			snack_word_vecs.append(vec_list)
		
		output = {
			"snack": self.snack,
			"snack_word_vecs": snack_word_vecs,
		}

		return output
