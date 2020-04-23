from PIL import Image
im = Image.open("images/encoded_sample.png")
im.rotate(45).show()