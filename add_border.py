from simpleimage import SimpleImage

BORDER = 10
DEFAULT_FILE = 'images/simba-sq.jpg'

def main():
    filename = get_file()
    old_image = SimpleImage(filename)
    width = old_image.width
    height = old_image.height

    new_image = SimpleImage.blank(width + 2 * BORDER, height + 2 * BORDER)

    for pixel in new_image:
        pixel.green = 0
        pixel.blue = 0
        pixel.red = 0

    for x in range(width):
        for y in range(height):
            new_image.set_pixel(x + BORDER, y + BORDER, old_image.get_pixel(x, y))

    new_image.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()