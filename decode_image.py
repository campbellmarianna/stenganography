from PIL import Image


def decode_image(file_location):
    encoded_image = Image.open(file_location)
    # Get all the red
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for x in range(0, x_size):
        for y in range(0, y_size):
            r = red_channel.getpixel((x, y))
            b_red = bin(r)
            LSB = b_red[-1]
            if LSB == '1':
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)
    decoded_image.show()
    decoded_image.save("decoded_image.png")


if __name__ == '__main__':
    file_location = 'images/encoded_sample.png'
    print(decode_image(file_location))
