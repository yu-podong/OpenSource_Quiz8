from tkinter import *
import random

## 클래스 선언 부분 ##
class Shape:  # 부모 클래스
    color, width = '', 0
    shx1, shy1 = 0, 0

    def getColor(self):
        r = random.randrange(16, 256)
        g = random.randrange(16, 256)
        b = random.randrange(16, 256)
        return "#" + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]

    def drawShape(self):  # 하위 클래스에서 상속받아서 오버라이딩 ( 추상 메서드 )
        raise NotImplementedError

class Rectangle(Shape):  # 자식 클래스
    shapeWidth, shapeHeight = 0, 0
    object = []

    def __init__(self, x1, y1):
        self.shx1 = x1
        self.shy1 = y1
        self.color = self.getColor()
        self.width = random.randrange(1, 9)
        self.shapeWidth = random.randrange(20, 100)
        self.shapeHeight = random.randrange(20, 100)
        self.drawShape()

    def __del__(self):
        for obj in self.object:
            canvas.delete(obj)

    def drawShape(self):
        sx1, sy1, sx2, sy2 = [0] * 4
        squareList = []

        sx1 = self.shx1 - self.shapeWidth
        sy1 = self.shy1 - self.shapeHeight
        sx2 = self.shx1 + self.shapeWidth
        sy2 = self.shy1 + self.shapeHeight

        squareList.append(canvas.create_line(sx1, sy1, sx1, sy2, fill = self.color, width =self.width))
        squareList.append(canvas.create_line(sx1, sy2, sx2, sy2, fill = self.color, width =self.width))
        squareList.append(canvas.create_line(sx2, sy2, sx2, sy1, fill = self.color, width =self.width))
        squareList.append(canvas.create_line(sx2, sy1, sx1, sy1, fill = self.color, width =self.width))

        self.object = squareList

class Circle(Shape):
    object = None

    def __init__(self, x1, y1):
        self.shx1 = x1
        self.shy1 = y1
        self.color = self.getColor()
        self.width = random.randrange(1, 9)
        self.shapeWidth = random.randrange(20, 100)
        self.shapeHeight = random.randrange(20, 100)
        self.drawShape()

    def __del__(self):
        canvas.delete(self.object)

    def drawShape(self):
        # 원 그리기
        sx1, sy1, sx2, sy2 = [0] * 4

        sx1 = self.shx1 - self.shapeWidth
        sy1 = self.shy1 - self.shapeHeight
        sx2 = self.shx1 + self.shapeWidth
        sy2 = self.shy1 + self.shapeHeight

        self.object = canvas.create_oval(sx1, sy1, sx2, sy2, outline = self.color, width = self.width)

## 함수 선언 부분 ##
def getWidth():
    return random.randrange(1, 9)

def createRectangle(event):
    global rectangleShape
    rect = Rectangle(event.x, event.y)
    rectangleShape.append(rect)

def createCircle(event):
    global circleShape
    circle = Circle(event.x, event.y)
    circleShape.append(circle)

def deleteRectangle(event):
    global rectangleShape
    if len(rectangleShape) != 0:
        temp = rectangleShape.pop()
        del temp

def deleteCircle(event):
    global circleShape
    if len(circleShape) != 0:
        temp = circleShape.pop()
        del temp

## 전역 변수 선언 ##
circleShape = []
rectangleShape = []
window = None
canvas = None

## 메인 코드 부분 ##
window = Tk()
window.title('객체지향 그림판(수정)')
canvas = Canvas(window, height=500, width=1000)
canvas.bind("<Double-Button-2>", deleteRectangle)
canvas.bind("<Double-Button-1>", deleteCircle)
canvas.bind("<Button-1>", createRectangle)
canvas.bind("<Button-3>", createCircle)

canvas.pack()
window.mainloop()