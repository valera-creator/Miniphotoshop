from PIL import Image


def makeanagliph(filename, delta):
    im1 = Image.open(filename)
    pixels_1 = im1.load()
    x, y = im1.size
    im2 = im1.copy()
    pixels_2 = im2.load()
    for i in range(x):
        for j in range(y):
            '''удаление красного'''
            r, g, b = pixels_2[i, j]
            r = 0
            pixels_2[i, j] = r, g, b
    for i in range(delta, x):
        for j in range(y):
            '''замена'''
            r2, g2, b2 = pixels_2[i, j]
            r1, g1, b1 = pixels_1[i - delta, j]
            pixels_2[i, j] = r1, g2, b2
    im2.save("result.jpg")


makeanagliph(filename='image.jpeg', delta=10)
