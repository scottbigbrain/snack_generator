import math
import numpy as np



# all vecs must be the same number of dimensions
def mean_coordinate(vecs):
	total = []
	for i in range(len(vecs[0])):
		total.append(0)

	for i in range(len(vecs)):

		for j in range(len(vecs[i])):
			total[j] += vecs[i][j]

	m = []
	for i in range(len(total)):
		m.append(total[i] / len(vecs))

	mean = np.array(m)

	return mean


def dist_between(vec1, vec2):

	triangle_lengths = []
	for i in range(len(vec1)):
		triangle_lengths.append(vec1[i] - vec2[i])


	total = 0
	for i in range(len(triangle_lengths)):
		value = triangle_lengths[i]
		total += sq(value)

	output = math.sqrt(total)
	return output


def sq(num):
	return num * num


def chunks(l, n):
    return [ l[i:i+n] for i in range(0, len(l), n) ]
