# Image Pixelator and Palette Creator
A python script that turns an image into a pixelated image using Pillow. It's a simple program that takes an image as input, makes it smaller, extracts every color of the smaller image and with that creates an **image that looks pixelated**

## How to use
- Clone the repository and install the requirements.txt with pip
- There are two ways of using it:
  - **Command line**: you can pass the arguments needed to run the program via command line, which are taken with `sys.argv`. For instance: `python3 my_image.jpg test1.jpg 100`. Now, if you want to input an url by this mode, you must add something after the last parameter, whatever you want (like a single letter) so the program knows it is an url and not a file.
  - Modify the `main.py` file and put your own parameters in the code.
- Note that the program works with image files as input and also with urls linking to images.

## How to create color palettes with the script
- An awesome thing about this is that you can create color palettes from an image with the same process as pixelating it. The only thing you need to do is to use a much smaller number of columns like 6 or 10, and you will get palettes for each image you want.
- The result will, of course, be an image with some colors, but just changing the code a bit, you can get the rgb of each pixel if you need.

