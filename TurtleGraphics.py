#TurtleGraphics.py
#Name:Miguel Alvarado
#Date: 2/15/2026
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(miggy, size):
    for i in range(4):
        miggy.forward(size)
        miggy.right(90)

def drawPolygon(miggy, sides):
    for s in range(sides):
        miggy.forward(50)
        miggy.right(360/sides)
        


    # drawPolygon(miggy, 5) #draws a pentagon
    # drawPolygon(miggy, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

def fillCorner(miggy, corner):
    drawSquare(miggy, 100)
    
    miggy.forward(50)
    miggy.right(90)
    miggy.forward(100)
    miggy.backward(100)
    miggy.left(90)
    miggy.backward(50)
    
    miggy.right(90)
    miggy.forward(50)
    miggy.left(90)
    miggy.forward(100)
    miggy.backward(100)
    miggy.right(90)
    miggy.backward(50)
    miggy.left(90)
    
    
    
    
    if corner == 1:
        miggy.begin_fill()
        drawSquare(miggy, 50)
        miggy.end_fill()
        
        
    elif corner == 2:
        miggy.forward(50)
        miggy.begin_fill()
        drawSquare(miggy, 50)
        miggy.end_fill()
        miggy.forward(50)
        
        
    elif corner == 3:
        miggy.right(90)
        miggy.forward(50)
        miggy.left(90)
        miggy.begin_fill()
        drawSquare(miggy, 50)
        miggy.end_fill()
        miggy.left(90)
        miggy.backward(50)
        miggy.right(90)
        
        
    elif corner == 4:
        miggy.forward(100)
        miggy.left(90)
        miggy.backward(100)
        miggy.left(90)
        miggy.begin_fill()
        drawSquare(miggy, 50)
        miggy.end_fill()
        miggy.left(90)
        miggy.right(90)

    fillCorner(miggy, 1)
    #fillCorner(miggy, 2)
    #fillCorner(miggy, 3)
    #fillCorner(miggy, 4)



    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
def squaresInSquares(miggy, num):
    size = 100

    for i in range(num):
        drawSquare(miggy, size)
        size = size + 35

        miggy.up()
        miggy.backward(20)
        miggy.left(90)
        miggy.forward(20)
        miggy.right(90)
        miggy.down()

    # squaresInSquares(miggy, 5) #draws 5 concentric squares
    # squaresInSquares(miggy, 3) #draws 3 concentric squares

def main():
    miggy = turtle.Turtle()

main()
