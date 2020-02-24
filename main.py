from PIL import Image as img


def find_possible(num, have_to):
    while have_to % num:
        have_to += 1
    return have_to


def main(file, save_to, cols_number):#The higher cols_number is, the higher is the number of pixels in the result image, and the more definition it has.
    origin = img.open(file, "r")
    or_width, or_height = origin.size #If the image is bigger, the time of execution will be more.

    resized = origin.resize((cols_number, int(or_height / (or_width / cols_number))))

    new_width = find_possible(resized.width, or_width)
    new_height = find_possible(resized.height, or_height)

    origin = img.new("RGB", (new_width, new_height), "red")

    scale_w = int(new_width / resized.width)
    scale_h = int(new_height / resized.height)

    finish_w = 0
    finish_h = 0

    for x in range(resized.width):
        finish_w += scale_w
        for y in range(resized.height):
            pix_color = resized.getpixel((x, y))
            finish_h += scale_h
            for w in range(finish_w - scale_w, finish_w + 1):
                if w >= origin.width:
                    continue
                for h in range(finish_h - scale_h, finish_h + 1):
                    if h >= origin.height:
                        continue
                    origin.putpixel((w, h), pix_color)

        finish_h = 0

    origin.save(save_to)


if __name__ == "__main__":
    main(r"Examples\ex3.png", r"Examples\ex3b.png", 40)
