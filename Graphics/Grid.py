class Grid:
	def __init__(self, _length, _width, _grid_size):
		self.length = _length
		self.width = _width
		self.grid_size = _grid_size
		self.elements = {}
		self.grid = []
		for row in range(self.length//self.grid_size):
			self.grid.append([])
			for col in range(self.width//self.grid_size):
				self.grid[row].append([])

	def add_element(self, new_element, row, col):
		self.elements[new_element] = (row,col)
		self.grid[row][col].append(new_element)
