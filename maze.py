import random
from time import sleep
from cell import Cell
from graphics import Point

class Maze:
	def __init__(
			self,
			top_left,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win = None,
			seed = None,
		):
		if seed is not None:
			random.seed(seed)
		self.__top_left = top_left
		self.__num_rows = num_rows
		self.__num_cols = num_cols
		self.__cell_size_x = cell_size_x
		self.__cell_size_y = cell_size_y
		self.__win = win

		self._create_cells()
		self._break_entrance_and_exit()
		self._break_walls_r(0, 0)
		self._reset_cells_visited()
	
	def _create_cells(self):
		self._cells = []
		x = self.__top_left.x
		for col in range(self.__num_cols):
			column = []
			self._cells.append(column)
			y = self.__top_left.y
			for row in range(self.__num_rows):
				cell = Cell(
					Point(x, y), 
					Point(x + self.__cell_size_x, y + self.__cell_size_y), 
					self.__win
					)
				column.append(cell)
				y += self.__cell_size_y
			x += self.__cell_size_x
		self._draw_cells()

	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top_wall = False
		self._draw_cell(0, 0)
		self._cells[-1][-1].has_bottom_wall = False
		self._draw_cell(-1, -1)
	
	def _break_walls_r(self, i, j):
		self._cells[i][j].visited = True
		current = self._cells[i][j]
		current.visited = True

		while True:
			to_visit = self._find_possible_coords(i, j)
			if len(to_visit) == 0:
				self._draw_cell(i, j)
				return

			direction = random.randint(0, len(to_visit) - 1)
			to_i, to_j = to_visit[direction]
			to_cell = self._cells[to_i][to_j]

			if to_i > i:
				current.has_right_wall = False
				to_cell.has_left_wall = False
			elif to_i < i:
				current.has_left_wall = False
				to_cell.has_right_wall = False
			elif to_j > j:
				current.has_bottom_wall = False
				to_cell.has_top_wall = False
			else:
				current.has_top_wall = False
				to_cell.has_bottom_wall = False

			self._break_walls_r(to_i, to_j)

	def _find_possible_coords(self, i, j):
		check_coords = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
		return list(filter(
					lambda i_j: 
		   				0 <= i_j[0] < self.__num_cols 
						and 0 <= i_j[1] < self.__num_rows 
						and not self._cells[i_j[0]][i_j[1]].visited, 
					check_coords)
				)

	def _reset_cells_visited(self):
		for col in self._cells:
			for cell in col:
				cell.visited = False

	def _draw_cell(self, x, y):
		cell = self._cells[x][y]
		cell.draw()
		self._animate()	
	
	def _draw_cells(self):
		for col in self._cells:
			for cell in col:
				cell.draw()
				self._animate()
	
	def _animate(self):
		if self.__win is None:
			return
		self.__win.redraw()
		sleep(0.05)

	def _solve_r(self, i, j):
		self._animate()
		current = self._cells[i][j]
		current.visited = True
		if i == self.__num_cols - 1 and j == self.__num_rows - 1:
			return True
		
		check_coords = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
		walls = [current.has_left_wall, current.has_right_wall, current.has_top_wall, current.has_bottom_wall]
		possible_coords = map(
				lambda i_j_wall: i_j_wall[0],
					filter(
						lambda i_j_wall: 
							not i_j_wall[1]
							and 0 <= i_j_wall[0][0] < self.__num_cols 
							and 0 <= i_j_wall[0][1] < self.__num_rows 
							and not self._cells[i_j_wall[0][0]][i_j_wall[0][1]].visited, 
						zip(check_coords, walls))
				)
		for to_i, to_j in possible_coords:
			print(f"trying: {to_i}, {to_j}")
			current.draw_move(self._cells[to_i][to_j])
			result = self._solve_r(to_i, to_j)
			if result:
				return True
			else:
				current.draw_move(self._cells[to_i][to_j], True)
		return False

	def solve(self):
		return self._solve_r(0, 0)