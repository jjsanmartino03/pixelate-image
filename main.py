from PIL import Image as img
import sys
import requests


def save_from_url(url, path):
    """
    Download an image from a url and save it in a determined file

    url     The url from which the image is requested
    path    Where the image will be saved
    """
    try:
        with open(path, "wb") as handle:
            response = requests.get(url, stream=True)

            if not response.ok:  # Something went wrong, abort
                return

            for pixel in response.iter_content(8192):  # iterate through the image
                if not pixel:  # End of the image, break loop
                    break
                handle.write(pixel)

        return True
    except:
        return False


def main(
    path_or_url, save_to, columns=50, url=False
    ):
    """
    Method for the pixelation of an image. It can be passed the path to a file or directly a url.

    path_or_url  The path to the image file or the link to the image
    save_to      The name of the file to which save the pixelated 
                 result
    columns      The higher number of columns is, the higher is the 
                 number of pixels in the result image, and the more 
                 definition it has. (also it is slower)
    """  
    if url:  # If the input is a link, call the method
        if not save_from_url(
            path_or_url, save_to
        ):  # Save it as temporary file, will be replaced later with the output
            return
        file = save_to
    else:
        file = path_or_url

    initial = img.open(file, "r")  # Open the image file with PIL
    # Note that if the image is bigger, the time of execution will be more.

    rows = int(
        initial.height / (initial.width / columns)
    )  # Calculate a proper number on rows based on the columns
    resized = initial.resize(
        (columns, rows)
    )  # This is done to only have the needed pixels and extract the colors from each one to form a pixelated image

    # The following calculations return what nuber of pixels should the image have so that it has an equal proportion to the resized image
    output_image_width = initial.width + (columns - initial.width % columns)
    output_image_height = initial.height + (rows - initial.height % rows)

    pixelated = img.new(
        "RGB", (output_image_width, output_image_height), "red"
    )  # Create a new image from zero with PIL

    # The following ratios indicate how many pixels of the new image will represent a single pixel of the resized one
    width_ratio = output_image_width // resized.width
    height_ratio = output_image_height // resized.height

    finish_w = 0
    finish_h = 0

    # The actual process here
    for x in range(resized.width):
        finish_w += width_ratio

        for y in range(resized.height):
            pix_color = resized.getpixel((x, y))

            finish_h += height_ratio
            for w in range(finish_w - width_ratio, finish_w + 1):
                if w >= pixelated.width:
                    continue

                for h in range(finish_h - height_ratio, finish_h + 1):
                    if h >= pixelated.height:
                        continue
                    pixelated.putpixel((w, h), pix_color)

        finish_h = 0

    pixelated.save(save_to)


if __name__ == "__main__":
    arguments = sys.argv
    if arguments[1:]:

        url_or_file = arguments[1]
        save_to = arguments[2]
        number_of_columns = int(arguments[3])
        is_url = False

        if len(arguments) > 4:
            is_url = True

        main(url_or_file, save_to, number_of_columns, is_url)
    else:
        pass # you can also pass the parameters from here and not from the CLI
        # main("", "", 50)
