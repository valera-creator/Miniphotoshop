from PIL import Image, ImageDraw


def board(num, size):
    im = Image.new("RGB", (num * size, num * size), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    y = 0
    for i in range(0, num, 2):
        for x in range(size, size * num, size * 2):
            draw.rectangle(((x, y), (x + size - 1, y + size - 1)), (255, 255, 255))
        y += size * 2
    y = size
    for i in range(1, num, 2):
        for x in range(0, size * num, size * 2):
            draw.rectangle(((x, y), (x + size - 1, y + size - 1)), (255, 255, 255))
        y += size * 2
    im.save("result.png")


board(num=8, size=50)
