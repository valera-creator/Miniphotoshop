from PIL import Image, ImageFilter


def image_filter(pixels_rainbov, pixels_usually, i, j):
    """эффект наложения полосок на картинку"""
    r1, g1, b1, *a = pixels_usually[i, j]
    r2, g2, b2, *a = pixels_rainbov[i, j]
    R = int(0.4 * r1 + 0.6 * r2)
    G = int(0.4 * g1 + 0.5 * g2)
    B = int(0.6 * b1 + 0.4 * b2)
    pixels_rainbov[i, j] = R, G, B
    return pixels_rainbov[i, j]


def rainbov_filter(pixels_rainbov, j, i, new_y):
    """создает радугу"""
    if j <= new_y:
        r = 255
        g = 0
        b = 0
    elif j <= new_y * 2 and j < new_y * 3:
        r = 255
        g = 126
        b = 0
    elif j <= new_y * 3 and j < new_y * 4:
        r = 235
        g = 255
        b = 3
    elif j <= new_y * 4 and j < new_y * 5:
        r = 42
        g = 255
        b = 100
    elif j <= new_y * 5 and j < new_y * 6:
        r = 0
        g = 0
        b = 255
    else:
        r = 157
        g = 0
        b = 255
    pixels_rainbov[i, j] = r, g, b
    return pixels_rainbov[i, j]


def blur(rainbov):
    """блюрит"""
    rainbov = rainbov.filter(ImageFilter.GaussianBlur(radius=4))
    return rainbov


def main(image_start, image_end):
    """
    :param image_start: путь к исходному изображению
    :param image_end: названия изображение после фильтра
    """

    im = Image.open(image_start)
    pixels_usually = im.load()
    x, y = im.size

    rainbov = Image.new("RGB", (x, y))
    new_y = int(y / 6)
    pixels_rainbov = rainbov.load()

    for j in range(y):
        for i in range(x):
            pixels_rainbov[i, j] = rainbov_filter(pixels_rainbov, j, i, new_y)

    for i in range(x):
        for j in range(y):
            pixels_rainbov[i, j] = image_filter(pixels_rainbov, pixels_usually, i, j)

    blur(rainbov)
    rainbov.save(image_end)


if __name__ == "__main__":
    main(image_start='start.jpg', image_end='end.jpg')
