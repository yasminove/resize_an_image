from PIL import Image

img = Image.open('baby.jpeg')

resized_img = img.resize((420, 420))

img.show()

resized_img.show()
