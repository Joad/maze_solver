import sys
from cell import Cell
from graphics import Window, Point
from maze import Maze

def main():
	win = Window(800, 600)
	maze = Maze(Point(10, 10), 10, 10, 30, 30, win)
	maze._break_entrance_and_exit()
	maze._break_walls_r(0, 0)
	maze._reset_cells_visited()
	maze.solve()
	win.wait_for_close()

if __name__ == "__main__":
	sys.exit(main())