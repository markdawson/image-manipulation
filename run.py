from PIL import Image
from random import random
import imageio


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
        offset = 2
        for x_offset in range(-offset, offset + 1):
            for y_offset in range(-offset, offset + 1):
                neighbor_pixel = im.getpixel((x + x_offset, y + y_offset))
                pixels.append(neighbor_pixel)

        return pixels
    except IndexError:
        return [im.getpixel((x, y))]

def apply_red_linear(im, image_name, red_amount):
    size = im.width * im.height

    print_points = [x * (size // 10) for x in range(1, 11)]

    i = 0
    for x in range(im.width):
        for y in range(im.height):
            i += 1

            if random() < red_amount:
                r, g, b = im.getpixel((x, y))
                im.putpixel((x, y), (255, g, b))

            if i in print_points:
                print(round((i / size), 1) * 100)

    im.save(image_name)


    return image_name

def apply_red_exponential(previous_image, image_name, red_amount):
    im = Image.open(previous_image)
    im = im.convert("RGB")
    size = im.width * im.height

    print_points = [x * (size // 10) for x in range(1, 11)]

    i = 0
    for x in range(im.width):
        for y in range(im.height):
            i += 1

            if random() < red_amount:
                r, g, b = im.getpixel((x, y))
                im.putpixel((x, y), (255, g, b))

            if i in print_points:
                print(round((i / size), 1) * 100)

    im.save(image_name)


    return image_name


def run():
    gif_linear = []
    gif_exponential =[]
    im = Image.open("images/Beach_Image_Small.png")
    im = im.convert("RGB")

    for i in range(10):
        each_image_linear = imageio.imread(apply_red_linear(im,"images/Beach_Image_Linear"+str(i)+".png",i*.1))# here read all images
        gif_linear.append(each_image_linear)
        each_image_exponential = imageio.imread(apply_red_exponential("images/Beach_Image_Expo"+str(i)+".png","images/Beach_Image_Expo"+str(i+1)+".png",i*.1))
        gif_exponential.append(each_image_exponential)
    
    imageio.mimsave("linear_result.gif", gif_linear, 'GIF')
    imageio.mimsave("exponential_result.gif", gif_exponential, 'GIF')

    # im.show()


if __name__ == "__main__":
    run()
    # print("done")
