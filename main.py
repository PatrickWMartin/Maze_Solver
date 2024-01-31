from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    win.wait_for_close()


main()
