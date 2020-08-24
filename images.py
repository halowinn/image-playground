from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
#filtered_img = img.filter(ImageFilter.DETAIL)
# filtered_img = img.convert('L')
# crop = filtered_img.crop((100, 100, 400, 400))
# crop.save('greypika.png', 'png')
# filtered_img.save('greypika.jpg')
# filtered_img.show()

# print(img.size)

img.thumbnail((400, 400))
img.save('thumbnail.jpg')

