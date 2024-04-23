import turtle as tr

tr.screensize(900, 800)
tr.shape('turtle')
tr.tracer(2)
tr.speed(1_000)


def go_to_center(x_of_center, y_of_center):
    tr.goto(x_of_center, y_of_center)
    tr.left(90)


def paint_vertical_grid(xv, yv, num_of_lines_v):
    tr.right(90)

    for _ in range(num_of_lines_v):
        tr.goto(xv, yv)

        tr.down()
        tr.fd(800)
        tr.up()
        xv += 1_320 // (num_of_lines_v - 1)


def paint_horizontal_grid(xh, yh, num_of_lines_h):
    tr.left(90)

    for _ in range(num_of_lines_h):
        tr.goto(xh, yh)

        tr.down()
        tr.fd(1_320)
        tr.up()
        yh -= 800 // (num_of_lines_h - 1)


def paint_main_axis(x_of_center, y_of_center):
    tr.color('#000000')

    tr.goto(x_of_center, -400)
    tr.left(90)
    tr.down()
    tr.fd(800)
    tr.up()

    tr.goto(-660, y_of_center)
    tr.right(90)
    tr.down()
    tr.fd(1_320)
    tr.up()

    go_to_center(x_of_center, y_of_center)


tr.up()
tr.color('#ff9191')

paint_vertical_grid(-660, 400, 133)

paint_horizontal_grid(-660, 400, 81)

paint_main_axis(0, 0)

tr.exitonclick()
