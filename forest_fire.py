"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
We’re going to start by writing a function called find_flames that
highlights the areas where a forest fire is active. Detect all of the
“sufficiently red” pixels in the image, which are indicative of where fires are burning in the image.
When you detect a “sufficiently red” pixel in the original image, you set its red value to
255 and its green and blue values to 0. This will highlight the pixel by making it entirely
red. For all other pixels (i.e., those that are not “sufficiently red”), you should convert
them to their grayscale equivalent, so that we can more easily see where the fire is
originating from. You can grayscale a pixel by summing together its red, green, and blue
values and dividing by three (finding the average), and then setting the pixel’s red, green,
and blue values to all have this same “average” value.
Once you highlight the areas that are on fire in the image (and greyscale all the remaining
pixels), you should see an image like that shown on the right in the image bellow. On the
left side of Figure 1, we should the original image for comparison.
Original forest fire image on left, and highlighted version of image on right.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage
DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames(filename):
    """
    This function highlights the "sufficiently red" pixels in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires. Grayscale averages the image color intensity so it looks like grey.
    """
    image = SimpleImage(filename)
    for pixel in image:
            average = (pixel.red + pixel.green + pixel.blue) // 3
            # See if this pixel is "sufficiently" red
            if pixel.red >= average:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = average
                pixel.green = average
                pixel.blue = average
    return image

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()

    
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
