from PIL import Image, ImageDraw


def make_image(filename):
    im = Image.new("RGB", (1320, 605), (41, 41, 255))
    draw = ImageDraw.Draw(im)
    x, y = im.size

    for i in range(120):
        if i <= 30:
            draw.line((0, i, 1320, i), fill="green")
        elif 30 < i <= 60:
            draw.line((0, i, 1320, i), fill="blue")
        elif 60 < i <= 90:
            draw.line((0, i, 1320, i), fill="#e3256b")
        else:
            draw.line((0, i, 1320, i), fill="orange")
    for i in range(0, 43):
        draw.line((i, 120, i, 605), fill="white")
    for i in range(1270, x):
        draw.line((i, 120, i, 605), fill="white")

    for i in range(43, 273):
        draw.line((i, 120, i, 605), fill=(75, 75, 75))
    for i in range(272, 590):
        draw.line((i, 120, i, 605), fill="green")
    for i in range(591, 950):
        draw.line((i, 120, i, 605), fill="yellow")
    for i in range(951, 1102):
        draw.line((i, 120, i, 605), fill=(0, 0, 255))
    for i in range(1102, x - 40):
        draw.line((i, 120, i, 605), fill=(75, 75, 75))

    draw.arc(xy=(5, 120, 255, 383), start=-90, end=-270, width=30, fill="white")
    draw.arc(xy=(5, 355, 255, 605), start=-90, end=-270, width=30, fill="green")
    for x in range(90, 130):
        draw.line((x, 120, x, 605), fill="#f400a1")

    draw.line((310, 470, 375, 470), fill="#ff1493", width=10)
    draw.line((310, 450, 375, 450), fill="#ff1493", width=10)
    draw.line((310, 460, 375, 460), fill=(75, 255, 0), width=15)
    draw.line((380, 122, 280, 605), fill="red", width=20)
    draw.line((398, 120, 398, 605), fill="#f8f32b", width=50)

    draw.line((500, 590, 590, 590), fill="red", width=30)
    for i in range(120, 606):
        if i < 200:
            draw.line((480, i, 510, i), fill="blue")
        elif 200 < i < 300:
            draw.line((480, i, 510, i), fill="red")
        elif 300 < i < 400:
            draw.line((480, i, 510, i), fill="blue")
        elif 400 < i < 500:
            draw.line((480, i, 510, i), fill="red")
        elif i > 500:
            draw.line((480, i, 510, i), fill="blue")

    for i in range(125, 550, 95):
        draw.ellipse(((605, i), (700, i + 95)), fill="blue")
    for i in range(125, 550, 190):
        draw.ellipse(((705, i), (800, i + 95)), fill="red")
        draw.ellipse(((805, i), (900, i + 95)), fill="green")

    draw.line((940, 120, 940, 605), fill=(75, 75, 75), width=50)
    draw.arc(xy=(830, 120, 1100, 400), start=-90, end=-270, width=30, fill="#ef0097")

    draw.line((1160, 470, 1250, 470), fill=(75, 255, 0), width=10)
    draw.line((1160, 450, 1250, 450), fill=(75, 255, 0), width=10)
    draw.line((1160, 460, 1250, 460), fill="#ff1493", width=20)
    draw.line((1180, 119, 1270, 605), fill="#f8f32b", width=20)
    draw.line((1150, 120, 1150, 605), fill="red", width=50)

    im.save(filename)


make_image(filename='name.png')
