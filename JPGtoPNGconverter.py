import sys
import os
from PIL import Image

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

if not os.path.exists(png_folder):
	os.makedirs(png_folder)

for filename in os.listdir(jpg_folder):
	img = Image.open(f'{jpg_folder}{filename}')
	clean_filename = os.path.splitext(filename)[0]
	img.save(f'{png_folder}{clean_filename}.png', 'png')

print('ALL DONE!')