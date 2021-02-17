from PIL import Image


def downsize(name, downsize_factor=4):
    im = Image.open(name)
    new_width = im.width // downsize_factor
    new_height = im.height // downsize_factor
    im = im.resize((new_width, new_height))
    im.save(name)


def run():
    im = Image.open("Beach_Image_Small.png")
    im = im.convert("RGB")

    # print(im.format, im.size, im.mode)

    size = im.width * im.height

    print_points = [x * (size // 10) for x in range(1, 11)]

    i = 0
    for x in range(im.width):
        for y in range(im.height):
            i += 1

            # Important Part
            r, g, b = im.getpixel((x, y))
            im.putpixel((x, y), (r + 15, g, b))

            if i in print_points:
                print(round((i / size), 1) * 100)

    im.save("Beach_Image_Small2.png")
    im.show()


if __name__ == "__main__":
    run()
    # print("done")

