#!/usr/bin/python

#===============================================================================
#          FILE: merge.py
#
#         USAGE: python merge.py
#
#   DESCRIPTION: Makes a merge between two images
#
#       OPTIONS: ---
#  REQUIREMENTS: Python Imaging Library (PIL)
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Jacinto Filipe - jacinto.filipe at ufpe.br
#  ORGANIZATION: ---
#       CREATED: 03/22/2013 11:41:00 AM BRT
#      REVISION:  ---
#===============================================================================
import os
import re
from PIL import Image

FILE_EXTENSIONS = ['.png','.jpg','.bmp','.gif']
IMAGE_SIZE = [0,0]
DEFAULT_FILE_NAME = 'output.png'
DEFAULT_BORDER = 3
DEFAULT_BACKGROUND_COLOR = 'black'
SEPARATOR = '/'
RESIZE = 0

ORIENTATION = int(raw_input('Set orientation (0 = HORIZONTAL | 1 = VERTICAL) : '))
RESIZE = int(raw_input('Would you like to set the image\'s size ? (0 = NO | 1 = YES) : '))

if RESIZE:
	new_size = raw_input('Set the dimensions as (WIDTH,HEIGHT), e.g. (200,250) : ')
	new_size = tuple(int(v) for v in re.findall("[0-9]+", new_size))

files = sorted([file for file in os.listdir(os.getcwd()) for extension in FILE_EXTENSIONS if file.endswith(extension)])

for file_name in files:
	image = Image.open(file_name)
	size = image.size
	IMAGE_SIZE[ORIENTATION] = IMAGE_SIZE[ORIENTATION] + size[ORIENTATION] + DEFAULT_BORDER
	if size[1-ORIENTATION] > IMAGE_SIZE[1-ORIENTATION] :
		IMAGE_SIZE[1-ORIENTATION] = size[1-ORIENTATION]

new_image = Image.new("RGBA", (IMAGE_SIZE[0],IMAGE_SIZE[1]), DEFAULT_BACKGROUND_COLOR)
coordinates = [0,0]
number = 1

for file_name in files:
	image = Image.open(file_name)
	size = image.size

	new_image.paste(image,(coordinates[0],coordinates[1]))
	coordinates[ORIENTATION] = coordinates[ORIENTATION] + size[ORIENTATION] + DEFAULT_BORDER

print "PATH %s"%(os.getcwd()+SEPARATOR+DEFAULT_FILE_NAME)

if RESIZE:
	new_image = new_image.RESIZE(new_size,Image.ANTIALIAS)

new_image.save(os.getcwd()+SEPARATOR+DEFAULT_FILE_NAME)
