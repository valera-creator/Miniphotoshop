from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color="#75BBFD", snow_color="#FFFAFA", trunk_color="#A45A52",
            needls_color="#01796F", sun_color="#FFDB00"):
    im = Image.new("RGB", (width, height), sky_color)
    draw = ImageDraw.Draw(im)
    y_snow = int(height * 0.8)
    for i in range(y_snow, height):
        draw.line((0, i, width, i), snow_color)

    x_up_sun = width - width * 0.2  # солнце
    y_up_sun = - (height - height * 0.8)
    x_down_sun = width + width * 0.2
    y_down_sun = height - height * 0.8
    draw.ellipse(((x_up_sun, y_up_sun), (x_down_sun, y_down_sun)), sun_color)

    x1_s = width * 0.45  # ствол
    y1_s = height * 0.9
    x2_s = width * 0.55
    y2_s = y1_s
    x3_s = x1_s
    y3_s = height * 0.7
    x4_s = x2_s
    y4_s = y3_s
    draw.polygon(((x1_s, y1_s), (x2_s, y2_s), (x4_s, y4_s), (x3_s, y3_s)), trunk_color)

    # зеленая штука 1
    x1_z1 = width * 0.3  # низ лево
    y1_z1 = height * 0.7
    y2_z1 = y1_z1  # низ право
    x2_z1 = width * 0.7
    x3_z1 = width * 0.3 + width * 0.1  # верх лево
    y3_z1 = height * 0.5
    y4_z1 = y3_z1  # верх право
    x4_z1 = width * 0.6
    draw.polygon(((x1_z1, y1_z1), (x2_z1, y2_z1), (x4_z1, y4_z1), (x3_z1, y3_z1)), needls_color)

    # зеленая штука 2
    x1_z2 = width * 0.35
    y1_z2 = height * 0.5
    y2_z2 = y1_z2
    x2_z2 = width * 0.65
    x3_z2 = width * 0.45
    y3_z2 = height * 0.3
    y4_z2 = y3_z2
    x4_z2 = width * 0.55
    draw.polygon(((x1_z2, y1_z2), (x2_z2, y2_z2), (x4_z2, y4_z2), (x3_z2, y3_z2)), needls_color)

    # зеленая штука 3
    x1 = width * 0.4
    y1 = height * 0.3
    x2 = width * 0.6
    y2 = y1
    x3 = width * 0.5
    y3 = height * 0.1
    draw.polygon(((x1, y1), (x2, y2), (x3, y3)), needls_color)
    im.save(file_name)


picture(file_name='result.png', width=1000, height=800)
