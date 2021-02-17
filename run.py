from PIL import Image
from random import random


def downsize(name, downsize_factor=4):
    im = Image.open(name)
    new_width = im.width // downsize_factor
    new_height = im.height // downsize_factor
    im = im.resize((new_width, new_height))
    im.save(name)


def get_pixel_neighbors(im, x, y):
    try:
        # pixels = [
        #     im.getpixel((x - 1, y - 1)),
        #     im.getpixel((x - 1, y)),
        #     im.getpixel((x - 1, y + 1)),
        #
        #     im.getpixel((x, y - 1)),
        #     im.getpixel((x, y + 1)),
        #
        #     im.getpixel((x + 1, y - 1)),
        #     im.getpixel((x + 1, y)),
        #     im.getpixel((x + 1, y + 1)),
        # ]

        pixels = []
        for x_offset in range(-5, 6):
            for y_offset in range(-5, 6):
                neighbor_pixel = im.getpixel((x + x_offset, y + y_offset))
                pixels.append(neighbor_pixel)

        return pixels
    except IndexError:
        return [im.getpixel((x, y))]




def run():
    im = Image.open("Beach_Image_Small.png")
    im = im.convert("RGB")

    size = im.width * im.height

    print_points = [x * (size // 10) for x in range(1, 11)]

    i = 0
    for x in range(im.width):
        for y in range(im.height):
            i += 1

            # Important Part
            # r, g, b = im.getpixel((x, y))

            neighbors = get_pixel_neighbors(im, x, y)

            # [(r, g, b), (r, g, b)... ]

            avg_r = round(sum(p[0] for p in neighbors) / len(neighbors))
            avg_g = round(sum(p[1] for p in neighbors) / len(neighbors))
            avg_b = round(sum(p[2] for p in neighbors) / len(neighbors))

            im.putpixel((x, y), (avg_r, avg_g, avg_b))

            if i in print_points:
                print(round((i / size), 1) * 100)

    im.save("Beach_Image_Small2.png")
    im.show()


if __name__ == "__main__":
    run()
    # print("done")
