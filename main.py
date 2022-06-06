from PIL import Image

def mean_filter(photo, filter_size):
    pixels = list(photo.getdata())
    width, height = photo.size

    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    SAT = [[0] * width for i in range(height)]

    SAT[0][0] = pixels[0][0]
    for H in range(height - 1):
        for W in range(width - 1):
            SAT[H + 1][W + 1] = pixels[H + 1][W + 1] + SAT[H][W + 1] + \
                                SAT[H + 1][W] - SAT[H][W]

    pixel_list = []
    for H in range(height):
        for W in range(width):
            if H >= filter_size and W >= filter_size:
                pixel_list.append(round((SAT[H][W] + SAT[H - filter_size][W - filter_size] -
                                         SAT[H - filter_size][W] - SAT[H][W - filter_size]) / (
                                                    filter_size * filter_size)))

    new_img = Image.new("L", (width - filter_size, height - filter_size))
    new_img.putdata(pixel_list)
    return new_img

if __name__ == '__main__':

    photo = Image.open("road.jpg")
    photo = photo.convert("L")

    mean_filter(photo, 71).show()