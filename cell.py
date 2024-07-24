from graphics import Line, Point

class Cell:

    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "grey"

        from_half = abs(self._x2 - self._x1) // 2
        from_x_centre = from_half + self._x1
        from_y_centre = from_half + self._y1

        to_half = abs(to_cell._x2 - to_cell._x1) // 2
        to_x_centre = to_half + to_cell._x1
        to_y_centre = to_half + to_cell._y1

        from_point = Point(from_x_centre, from_y_centre)
        to_point = Point(to_x_centre, to_y_centre)
        line = Line(from_point, to_point)
        self._win.draw_line(line, line_color)