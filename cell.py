from graphics import Line, Point

class Cell:
	def __init__(
			self,
			top_left,
			bottom_right,
			window = None
		):
		self.has_left_wall = True 
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self.visited = False
		self.__top_left = top_left
		self.__bottom_left = Point(top_left.x, bottom_right.y)
		self.__top_right = Point(bottom_right.x, top_left.y)
		self.__bottom_right = bottom_right
		self.__win = window

	def draw(self):
		if self.__win is None:
			return
		
		left_wall = Line(self.__top_left, self.__bottom_left)
		if self.has_left_wall:
			self.__win.draw_line(left_wall)
		else:
			self.__win.draw_line(left_wall, "white")

		right_wall = Line(self.__top_right, self.__bottom_right)
		if self.has_right_wall:
			self.__win.draw_line(right_wall)
		else:
			self.__win.draw_line(right_wall, "white")
		
		top_wall = Line(self.__top_right, self.__top_left)
		if self.has_top_wall:
			self.__win.draw_line(top_wall)
		else:
			self.__win.draw_line(top_wall, "white")

		bottom_wall = Line(self.__bottom_right, self.__bottom_left)
		if self.has_bottom_wall:
			self.__win.draw_line(bottom_wall)
		else:
			self.__win.draw_line(bottom_wall, "white")

	def draw_move(self, to_cell, undo=False):
		if self.__win is None:
			return
		middle1 = self.__top_left.middle(self.__bottom_right)
		middle2 = to_cell.__top_left.middle(to_cell.__bottom_right)
		line = Line(middle1, middle2)
		self.__win.draw_line(line, "gray" if undo else "red")