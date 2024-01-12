import unittest
from graphics import Point
from maze import Maze

class Tests(unittest.TestCase):
	def test_maze_create_cells(self):
		num_cols = 12
		num_rows = 10
		m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
		self.assertEqual(
			len(m1._cells),
			num_cols
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_rows
		)
	
	def test_maze_no_cells(self):
		num_cols = 0
		num_rows = 0
		m1 = Maze(Point(0, 0), num_cols, num_rows, 10, 10)
		self.assertEqual(
			len(m1._cells),
			num_cols
		)

	def test_break_entrance_and_exit(self):
		num_cols = 10
		num_rows = 10
		m1 = Maze(Point(0, 0), num_cols, num_rows, 10, 10)
		m1._break_entrance_and_exit()
		self.assertEqual(
			m1._cells[0][0].has_top_wall,
			False
		)
		self.assertEqual(
			m1._cells[-1][-1].has_bottom_wall,
			False
		)

	def test_reset_visited(self):
		num_cols = 10
		num_rows = 10
		m1 = Maze(Point(0, 0), num_cols, num_rows, 10, 10, seed=1)
		m1._break_walls_r(0, 0)
		m1._reset_cells_visited()
		for col in m1._cells:
			for cell in col:
				self.assertEqual(cell.visited, False)


if __name__ == "__main__":
	unittest.main()