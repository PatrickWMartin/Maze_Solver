from tkinter import Tk, BOTH, Canvas
from typing import Type


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Type[Point], point2: Type[Point]):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, width: int, height: int):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="white",
                              height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self._running = False

    def draw_line(self, line: Type[Line], fill_color: str) -> None:
        line.draw(self._canvas, fill_color)
