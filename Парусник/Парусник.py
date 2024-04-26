from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535",
            sail_color="#FFFFFF", sun_color="#FFCF40"):
    im = Image.new("RGB", (width, height), sky_color)
    x, y = im.size
    draw = ImageDraw.Draw(im)
    ocean = int(y - y * 0.2)
    for i in range(x):
        for j in range(ocean, y):
            draw.line((0, j, width, j), fill=ocean_color)
    left_niz_x_boat = width - width * 0.7
    left_niz_y_boat = height - height * 0.15

    left_verx_x_boat = width - width * 0.75
    left_verx_y_boat = height - height * 0.35

    right_niz_x_boat = width - width * 0.3
    right_niz_y_boat = left_niz_y_boat

    right_verx_x_boat = width - width * 0.25
    right_verx_y_boat = left_verx_y_boat

    draw.polygon(
        ((left_verx_x_boat, left_verx_y_boat),
         (left_niz_x_boat, left_niz_y_boat),
         (right_niz_x_boat, right_niz_y_boat),
         (right_verx_x_boat, right_verx_y_boat)), fill=boat_color)

    palka_left_verx_x = width * 0.49
    palka_left_verx_y = height * 0.3

    palka_right_verx_x = width * 0.51
    palka_right_verx_y = height * 0.3

    palka_left_niz_x = palka_left_verx_x
    palka_left_niz_y = height * 0.75

    palka_right_niz_x = palka_right_verx_x
    palka_right_niz_y = height * 0.7

    draw.polygon(((palka_left_verx_x, palka_left_verx_y),
                  (palka_right_verx_x, palka_right_verx_y),
                  (palka_right_niz_x, palka_right_niz_y),
                  (palka_left_niz_x, palka_left_niz_y)), fill=boat_color)

    parys_verx_x = palka_right_verx_x
    parys_verx_y = palka_right_verx_y

    parys_right_x = parys_verx_x + width * 0.15
    parys_right_y = height * 0.45

    parys_niz_x = parys_verx_x
    parys_niz_y = height * 0.6

    draw.polygon(((parys_verx_x, parys_verx_y),
                  (parys_right_x, parys_right_y),
                  (parys_niz_x, parys_niz_y)), fill=sail_color)
    sun_verx_x = width - width * 0.2
    sun_verx_y = -(height - height * 0.8)
    sun_niz_x = width + width * 0.2
    sun_niz_y = height - height * 0.8
    draw.ellipse(((sun_verx_x, sun_verx_y), (sun_niz_x, sun_niz_y)), sun_color)
    im.save(f"{file_name}")


picture(file_name="result.png", width=1000, height=800)
