from turtle import *

cc = Screen()
Turt = Turtle()
Screen().listen()
Screen().addshape(".\src\pygamecre\sword.gif")
sword = Turtle(".\src\pygamecre\sword.gif")
sword.hideturtle()
sword.penup()
sword.goto(Turtle().pos())
enemy = Turtle()
enemy.hideturtle()
enemy.penup()
enemy.right(180)
enemy.goto(500.00, 0.00)

def key(keyname, action):
    global cc
    global Turt
    global sword
    global enemy
    if action == "forward":
        def forw():
            Turt.forward(90)
        Screen().onkeypress(forw, keyname)
    elif action == "backward":
        def backw():
            Turt.backward(90)
        Screen().onkeypress(backw, keyname)
    elif action == "left":
        def leftw():
            Turt().right(90)
        Screen().onkeypress(leftw, keyname)
    elif action == "right":
        def rightw():
            Turt.left(90)
        Screen().onkeypress(rightw, keyname)
    elif action == "attack":
        sword.showturtle()
        enemy.showturtle()
        sword.goto(enemy.pos())
    else:
        print("Action: There is no action named: " + action)

def dark_mode():
    global cc
    global Turt
    global sword
    global enemy
    cc.bgcolor("gray")

def imageLoad(root):
    global Turt
    global cc
    cc.addshape(root)
    Turt.shape(root)