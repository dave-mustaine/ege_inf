# import turtle
# import random
#
# turtle.shape('turtle')
#
# # # 1
# # turtle.goto(0, 0)
# # turtle.right(90)
# # turtle.fd(100)
# # turtle.left(90)
# # turtle.fd(100)
# # turtle.left(90)
# # turtle.fd(100)
# # turtle.left(90)
# # turtle.fd(100)
# #
# # turtle.up()
# # turtle.goto(120, 0)
# # turtle.down()
# #
# # turtle.right(180)
# # turtle.fd(100)
# # turtle.right(120)
# # turtle.fd(100)
# # turtle.right(120)
# # turtle.fd(100)
# #
# # turtle.up()
# # turtle.goto(120, 120)
# # turtle.down()
# #
# # turtle.right(120)
# # turtle.fd(100)
# # turtle.right(45)
# # turtle.fd(70)
# # turtle.right(135)
# # turtle.fd(100)
# # turtle.right(45)
# # turtle.fd(70)
# #
# # turtle.up()
# # turtle.goto(0, 120)
# # turtle.down()
# #
# # turtle.left(45)
# # turtle.fd(100)
# # turtle.left(180 - 36)
# # turtle.fd(100)
# # turtle.left(180 - 36)
# # turtle.fd(100)
# # turtle.left(180 - 36)
# # turtle.fd(100)
# # turtle.left(180 - 36)
# # turtle.fd(100)
# #
# # turtle.up()
# # turtle.goto(0, -120)
# # turtle.down()
# #
# # turtle.right(30 + 36)
# # turtle.fd(100)
# # turtle.right(180 - 60)
# # turtle.fd(100)
# # turtle.right(60)
# # turtle.fd(100)
# # turtle.right(120)
# # turtle.fd(100)
# #
# # turtle.exitonclick()
#
# # # 2
# # colors = '0123456789abcdef'
# # turtle.goto(0, 0)
# # for i in range(18):
# #     color_ = '#'
# #     for j in range(6):
# #         color_ += colors[random.randint(0, 15)]
# #     turtle.color(color_, color_)
# #
# #     turtle.begin_fill()
# #
# #     for k in range(4):
# #         turtle.fd(100)
# #         turtle.left(90)
# #     turtle.left(20)
# #
# #     turtle.end_fill()
# #
# # turtle.exitonclick()
#
# # # 3
# # def turt_dots():
# #     for __ in range(40):
# #         turtle.fd(10)
# #         turtle.dot(2)
# #
# #
# # turtle.tracer(0)
# # turtle.speed(100)
# # turtle.up()
# # turtle.goto(-200, 0)
# # turtle.down()
# #
# # turtle.fd(400)
# #
# # turtle.up()
# # turtle.goto(0, -200)
# # turtle.down()
# # turtle.left(90)
# #
# # turtle.fd(400)
# #
# # turtle.up()
# # turtle.goto(-200, 200)
# # turtle.right(90)
# #
# # for _ in range(11):
# #     turtle.dot(5)
# #
# #     turt_dots()
# #
# #     turtle.right(90)
# #     turtle.fd(20)
# #     turtle.right(90)
# #     turtle.dot(5)
# #
# #     turt_dots()
# #
# #     turtle.left(90)
# #     turtle.fd(20)
# #     turtle.left(90)
# #
# # turtle.goto(0, 0)
# # turtle.left(90)
# # turtle.down()
# #
# # turtle.color('red')
# # for _ in range(5):
# #     turtle.right(45)
# #     turtle.fd(100)
# #     turtle.right(45)
# #
# # turtle.color('blue')
# # for _ in range(6):
# #     turtle.fd(200)
# #     turtle.right(90)
# #
# #
# # turtle.exitonclick()
#
# turtle.color('red')
#
# for _ in range(2):
#     turtle.fd(70)
#     turtle.right(90)
#     turtle.fd(40)
#     turtle.right(90)
#
# turtle.up()
#
# turtle.fd(20)
# turtle.right(90)
# turtle.fd(50)
# turtle.left(90)
#
# turtle.down()
# turtle.color('blue')
#
# for _ in range(2):
#     turtle.fd(30)
#     turtle.right(90)
#     turtle.fd(40)
#     turtle.right(90)
#
# turtle.exitonclick()

import turtle as tr

tr.screensize(900, 800)
tr.shape('turtle')
tr.tracer(2)
tr.speed(100)


# def dots():
#     for _ in range(120):
#         tr.dot(3, 'red')
#         tr.fd(10)


# def rotate_when_dots():
#     for _ in range(40):
#         dots()
#
#         tr.dot(3, 'red')
#         tr.right(90)
#         tr.fd(10)
#         tr.right(90)
#
#         dots()
#
#         tr.dot(3, 'red')
#         tr.left(90)
#         tr.fd(10)
#         tr.left(90)

def vertical_lines(xv, yv):
    tr.goto(xv, yv)

    tr.down()
    tr.fd(800)
    tr.up()


def horizontal_lines(xh, yh):
    tr.goto(xh, yh)

    tr.down()
    tr.fd(1_320)
    tr.up()


tr.up()

tr.right(90)
tr.color('red')

x = -660
y = 400

for _ in range(67):
    vertical_lines(x, y)
    x += 20

tr.left(90)

x = -660
y = 400

for _ in range(41):
    horizontal_lines(x, y)
    y -= 20

tr.color('black')
tr.goto(0, -400)
tr.left(90)
tr.down()
tr.fd(800)
tr.up()

tr.goto(-660, 0)
tr.right(90)
tr.down()
tr.fd(1_320)
tr.up()

tr.left(90)
tr.color('cyan')
tr.goto(0, 0)
tr.down()

# for _ in range(7):  # https://education.yandex.ru/ege/task/2001c132-1204-4f86-bdba-8a21ea08391c
#     tr.fd(200)
#     tr.right(120)

for _ in range(9):  # https://education.yandex.ru/ege/task/d357aaaa-53b2-4348-bb4d-ee71688c114e
    tr.fd(300)
    tr.right(90)
    tr.fd(500)
    tr.right(90)

tr.up()
tr.left(180)
tr.fd(200)
tr.left(180)
tr.down()
tr.color('green')

for _ in range(8):
    tr.fd(300)
    tr.left(90)
    tr.fd(500)
    tr.left(90)

tr.up()
tr.fd(120)
tr.left(90)
tr.down()
tr.color('purple')

for _ in range(7):
    tr.fd(300)
    tr.right(90)
    tr.fd(500)
    tr.right(90)

tr.exitonclick()
