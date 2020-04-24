from PIL import Image 
def decode_image(file_location):
    # Returns an image object
    encoded_image = Image.open(file_location)
    print("encoded_image:", encoded_image)
    # Get all the red 
    red_channel = encoded_image.split()[0]
    print('red_channel:', red_channel)

    x_size = encoded_image.size[0]
    # print('x_size:', type(x_size))
    y_size = encoded_image.size[1]
    # print('y_size:', y_size)

    decoded_image = Image.new("RGB", encoded_image.size)
    # decoded_image.show()
    pixels = decoded_image.load()
    # print('pixels', type(pixels))
    # Fill in decoding functionality
    # iterate through each pixel in the encoded image and set the decode_image pixel to be (0,0,0) or (255,255,255) depending on the value of that LSB
    # Loop over the range of x_size (`x`)
    for x in range(0, x_size):
        # print("***x:", x)
        # Loop over the range of y_size (`y`)
        for y in range(0, y_size):
            # print("***y:", y)
            # coordinates = x, y
            # Get RGB values from red_channel via `getpixel(x, y)`
            # r = red_channel.getpixel(coordinates)
            # print("what is red_channel.getpixel(coordinates):",
            #       red_channel.getpixel(coordinates))
            r = red_channel.getpixel((x,y))
            # Convert red value in returned tuple to a binary string via `bin()`
            b_red = bin(r)
            # print("b_red", b_red)
            # Grab the LSB (right-most value) from the binary string
            LSB = b_red[-1]
            # print("LSB", LSB)
            # Perform a check to see if resulting LSB value is `1`
            #   Write `pixels[x, y]` to to black `(0, 0, 0)`
            if LSB == '1':
                # print('What does the pixel look like right now:', pixels[x, y])
                pixels[x,y] = (0, 0 , 0)
            # Otherwise
            #   Write `pixels[x, y]` to white `(255, 255, 255)`
            else:
                pixels[x,y] = (255, 255, 255)
    decoded_image.show()
    # Save the decoded image as `decoded_image.png`
    decoded_image.save("decoded_image.png")

if __name__ == '__main__':
    file_location = 'images/encoded_sample.png'
    print(decode_image(file_location))
