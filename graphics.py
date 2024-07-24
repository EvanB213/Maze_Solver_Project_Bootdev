from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver 3000")

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed..")
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:

    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
