from PIL import Image, ImageDraw


def gradient(color):
    """
    :param color: цвет градиента, может быть только R, G, B)
    """

    if color.lower() not in ('r', 'g', 'b'):
        quit('допустимые значения: R, G, B')

    gradient = -1
    im = Image.new("RGB", (512, 200), (0, 0, 0))
    pixels = im.load()
    draw = ImageDraw.Draw(im)
    x, y = im.size
    for i in range(0, x, 2):
        gradient += 1
        for j in range(y):
            r, g, b = pixels[i, j]
            if color.lower() == "r":
                r = gradient
            elif color.lower() == "g":
                g = gradient
            elif color.lower() == "b":
                b = gradient
        draw.line((i, 0, i, 200), fill=(r, g, b), width=2)
    im.save("res.png")


gradient(color='B')
