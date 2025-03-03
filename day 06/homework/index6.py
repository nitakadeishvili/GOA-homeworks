#დავალება 4

from turtle import*

import turtle

t = turtle.Turtle()
t.speed(3)

# ფუნქცია რომ დახატოს კედლები და ა.შ
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# მთავარი კედელი
draw_rectangle(-100, -100, 200, 100, "gray")

# მარცხენა
draw_rectangle(-120, 0, 40, 80, "darkgray")

# მარჯვენა
draw_rectangle(80, 0, 40, 80, "darkgray")

# კარები
draw_rectangle(-20, -100, 40, 60, "brown")

# ჯოხი დროშისთვის
t.penup()
t.goto(100, 80)
t.pendown()
t.pensize(3)
t.goto(100, 160)  # გრძელი ჯოხი

# დროშა
draw_rectangle(100, 120, 50, 40, "green")  # ოთხკუთხედი დროშაა

# ვწერთ GOAს დროშაში
t.penup()
t.goto(105, 130)  # Position on flag
t.pencolor("black")
t.write("GOA", font=("Arial", 15, "bold"))

# დამთავრება

t.hideturtle()
turtle.done()



