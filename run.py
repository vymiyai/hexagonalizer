from PIL import Image, ImageDraw, ImageColor


def load_image( image_file ):
	image = Image.open( image_file )
	#print(image.format, image.size, image.mode)
	#image.show()
	return ImageDraw.Draw(image)

def get_hexagon_points( hexagon_center ):
	return [(row-1,column-1), (row-1,column+1), (row,column+2), (row+1,column+1), (row+1,column-1), (row,column-2)]

def to_pixels( point_dictionary, hexagon_points ):
	try:
		return [ point_dictionary[ point ] for point in hexagon_points ]
	except KeyError:
		return []

import plotter

scale_factor = 4

image = Image.open( 'index.png' )
image = image.resize((image.width*scale_factor, image.height*scale_factor))
img_draw = ImageDraw.Draw(image)

points = plotter.plot(10, image.width, image.height)

points_in_pixels = []
hexagons = {}
for row, column in points.keys():
	# if the row number is even, an offset must be applied.
	point = (row, column)
	point_in_pixels = points[point]

	if (row % 2 != column % 2):
		# row is even.
		if (row % 2) == 0:
			if (column + 1) % 6 != 0:
				points_in_pixels.append( point_in_pixels )
			else:
				hexagons[ point ] = get_hexagon_points( point )
		# row is odd.
		else:
			if (column - 2) % 6 != 0:
				points_in_pixels.append( point_in_pixels )
			else:
				hexagons[ point ] = get_hexagon_points( point )

#print(points)
#print(points_in_pixels)
#print(list(hexagons.keys()))
#print(list(hexagons.values()))

hexes = []
for hex_points in list(hexagons.values()):
	pixels = to_pixels( points, hex_points )
	if len(pixels) != 0:
		img_draw.polygon( pixels, None, ImageColor.getrgb('black'))
	hexes = hexes + pixels

#img_draw.point(points_in_pixels, ImageColor.getrgb('black'))
img_draw.point( hexes, ImageColor.getrgb('white'))
#image.show()
image.save('improved.png')
