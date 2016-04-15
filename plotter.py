import math
from bidict import bidict

def plot(edge_length, width, height):
	x = 0
	y = 1
	starting_point = (0, 0)

	w = edge_length / 2
	h = math.sqrt( edge_length**2 - w**2 )

	number_of_columns = math.ceil( width / w )
	number_of_rows = math.ceil( height / h )
	

	points = bidict()



	for row in range(number_of_rows + 1):
		for column in range(number_of_columns + 1):
			points.put((row, column), (column*w, row*h))

	return points
