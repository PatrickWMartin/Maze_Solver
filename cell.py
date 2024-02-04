from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")

        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2,), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1,), Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")

    def draw_move(self, to_cell, undo: bool = False) -> None:
        fill_color = 'red'
        if undo:
            fill_color = 'grey'

        x_mid = (self._x1 + self._x2)/2
        y_mid = (self._y1 + self._y2)/2

        to_x_mid = (to_cell._x1 + to_cell._x2)/2
        to_y_mid = (to_cell._y1 + to_cell._y2)/2

        self._win.draw_line(
                Line(Point(x_mid, y_mid), Point(to_x_mid, to_y_mid)),
                fill_color)
