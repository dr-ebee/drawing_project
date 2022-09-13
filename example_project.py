from turtle import *

cat_eye_size = 10
whisker_length = 100

speed(0)
window = Screen()

"""
Draws a single cat eye, starting at the right corner of the eye

@size a factor to scale the eye by. If size is 10, then the eye is about 10
  pixels high
"""
def cat_eye(size):
    # Draw outline of the eye
    right(30)
    forward(5*size)
    right(120)
    forward(5*size)
    right(60)
    forward(5*size)
    right(120)
    forward(5*size)
    right(150)

    # Draw pupil of the eye
    forward(3*size)
    left(60)
    forward(3*size)
    left(120)
    forward(3*size)
    left(60)
    forward(3*size)

"""
Draws 2 cat eyes. Starts and ends in the center of both eyes
@size a factor to scale the eye by. If size is 10, then the eye is about 10
  pixels high
"""
def cat_eyes(size):
    # Move to the position of the first eye
    up()
    right(210)
    forward(6*size)
    left(210)
    # Draw the first (left) eye
    down()
    cat_eye(size)
    up()
    right(120)
    forward(10*size)
    # Draw the second (right) eye
    down()
    cat_eye(size)
    up()
    # Move back to the center
    right(210)
    forward(3*size)
    right(90)
    forward(5*size)

"""
Draws 3 whiskers, starting with the top whisker
"""
def whiskers():
    forward(60)
    left(20)
    # Draw each whisker a little bit longer than the previous one
    for i in range(3):
        down()
        forward(whisker_length + i*10)
        backward(whisker_length + i*10)
        up()
        right(90)
        forward(20)
        left(85)
    up()
    goto(-30, -80)
    right(180)
    # Draw each whisker a little bit longer than the previous one
    for i in range(3):
        down()
        forward(whisker_length + i*10)
        backward(whisker_length + i*10)
        up()
        right(90)
        forward(20)
        left(85)

# Draw eyes
cat_eyes(cat_eye_size)
left(90)
forward(30)

# Draw nose
down()
circle(10)
up()
right(90)
forward(100)
right(90)
right(180)

# Draw whiskers
down()
circle(100)
up()
left(90)
forward(100)
whiskers()


window.exitonclick()