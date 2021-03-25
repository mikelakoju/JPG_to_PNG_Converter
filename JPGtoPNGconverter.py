import sys
import os
from PIL import Image

'''
This program grab a JPG photo and converts it into a PNG.
You are required to pass in the folder that  contains the 
images and the new folder you wish to save the new converted images.

'''

# grab firdt and second argument
image_folder = sys.argv[1]

output_folder = sys.argv[2]


# chekc if new folder exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#print(image_folder, output_folder)

# Loop through pokedex,
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# convert images to png

# save to the new folder
