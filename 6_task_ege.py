import turtle
import random

turtle.shape('turtle')

# # 1
# turtle.goto(0, 0)
# turtle.right(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
#
# turtle.up()
# turtle.goto(120, 0)
# turtle.down()
#
# turtle.right(180)
# turtle.fd(100)
# turtle.right(120)
# turtle.fd(100)
# turtle.right(120)
# turtle.fd(100)
#
# turtle.up()
# turtle.goto(120, 120)
# turtle.down()
#
# turtle.right(120)
# turtle.fd(100)
# turtle.right(45)
# turtle.fd(70)
# turtle.right(135)
# turtle.fd(100)
# turtle.right(45)
# turtle.fd(70)
#
# turtle.up()
# turtle.goto(0, 120)
# turtle.down()
#
# turtle.left(45)
# turtle.fd(100)
# turtle.left(180 - 36)
# turtle.fd(100)
# turtle.left(180 - 36)
# turtle.fd(100)
# turtle.left(180 - 36)
# turtle.fd(100)
# turtle.left(180 - 36)
# turtle.fd(100)
#
# turtle.up()
# turtle.goto(0, -120)
# turtle.down()
#
# turtle.right(30 + 36)
# turtle.fd(100)
# turtle.right(180 - 60)
# turtle.fd(100)
# turtle.right(60)
# turtle.fd(100)
# turtle.right(120)
# turtle.fd(100)
#
# turtle.exitonclick()

# # 2
# colors = '0123456789abcdef'
# turtle.goto(0, 0)
# for i in range(18):
#     color_ = '#'
#     for j in range(6):
#         color_ += colors[random.randint(0, 15)]
#     turtle.color(color_, color_)
#
#     turtle.begin_fill()
#
#     for k in range(4):
#         turtle.fd(100)
#         turtle.left(90)
#     turtle.left(20)
#
#     turtle.end_fill()
#
# turtle.exitonclick()

# # 3
# def turt_dots():
#     for __ in range(40):
#         turtle.fd(10)
#         turtle.dot(2)
#
#
# turtle.tracer(0)
# turtle.speed(100)
# turtle.up()
# turtle.goto(-200, 0)
# turtle.down()
#
# turtle.fd(400)
#
# turtle.up()
# turtle.goto(0, -200)
# turtle.down()
# turtle.left(90)
#
# turtle.fd(400)
#
# turtle.up()
# turtle.goto(-200, 200)
# turtle.right(90)
#
# for _ in range(11):
#     turtle.dot(5)
#
#     turt_dots()
#
#     turtle.right(90)
#     turtle.fd(20)
#     turtle.right(90)
#     turtle.dot(5)
#
#     turt_dots()
#
#     turtle.left(90)
#     turtle.fd(20)
#     turtle.left(90)
#
# turtle.goto(0, 0)
# turtle.left(90)
# turtle.down()
#
# turtle.color('red')
# for _ in range(5):
#     turtle.right(45)
#     turtle.fd(100)
#     turtle.right(45)
#
# turtle.color('blue')
# for _ in range(6):
#     turtle.fd(200)
#     turtle.right(90)
#
#
# turtle.exitonclick()

turtle.color('red')

for _ in range(2):
    turtle.fd(70)
    turtle.right(90)
    turtle.fd(40)
    turtle.right(90)

turtle.up()

turtle.fd(20)
turtle.right(90)
turtle.fd(50)
turtle.left(90)

turtle.down()
turtle.color('blue')

for _ in range(2):
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(40)
    turtle.right(90)

turtle.exitonclick()

