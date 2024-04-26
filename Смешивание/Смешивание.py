from PIL import Image


def transparency(filename1, filename2):
    """
    :param filename1: путь до первого изображения
    :param filename2: путь до второго изображения
    """

    first_image = Image.open(filename1)
    pixels_first = first_image.load()
    x, y = first_image.size
    second_image = Image.open(filename2)
    pixels_second = second_image.load()
    for i in range(x):
        for j in range(y):
            R1, G1, B1, *a = pixels_first[i, j]
            R2, G2, B2, *a = pixels_second[i, j]
            R = int(R1 * 0.5 + R2 * 0.5)
            G = int(G1 * 0.5 + G2 * 0.5)
            B = int(B1 * 0.5 + B2 * 0.5)
            pixels_first[i, j] = R, G, B
    first_image.save("result.jpg")


transparency(filename1='first_image.jpeg', filename2='second_image.jpeg')
