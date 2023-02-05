from PySide6 import QtWidgets, QtGui, QtCore
import math



class GraphicScene(QtWidgets.QGraphicsScene):
	def __init__(self, scene, parent = None):
		super().__init__(parent)

		self.scene = scene

		BG_COLOR = ("#393939")
		LIGHT_COLOR = ("#2f2f2f")
		DARK_COLOR = ("292929")
		self.GRID_SIZE = 30
		self.GRID_SQUARE = 5

		# settings

		self.bg_color = QtGui.QColor(BG_COLOR)
		self.light_color = QtGui.QColor(LIGHT_COLOR)
		self.dark_color = QtGui.QColor(DARK_COLOR)


		self.penLight = QtGui.QPen(LIGHT_COLOR)
		self.penLight.setWidth(1)
		self.penDark = QtGui.QPen(LIGHT_COLOR)
		self.penDark.setWidth(2)

		
		self.setBackgroundBrush(self.bg_color)
		# self.draw_background()

	def set_graphic_scene(self, width, height):
		self.setSceneRect(-width // 2, -height // 2, width, height)






	def drawBackground(self, painter, rect):
		super().drawBackground(painter, rect)

		# create grid
		left = int(math.floor(rect.left()))
		right = int(math.floor(rect.right()))
		top = int(math.floor(rect.top()))
		bottom = int(math.floor(rect.bottom()))

		first_left = left - (left % self.GRID_SIZE)
		first_top = top - (top % self.GRID_SIZE)

		# compute all line to be drawn
		light_lines, dark_lines = [], []

		for x in range(first_left, right, self.GRID_SIZE):
			if x % (self.GRID_SIZE * self.GRID_SQUARE) != 0:
				light_lines.append(QtCore.QLine(x, top, x, bottom))
			else:
				dark_lines.append(QtCore.QLine(x, top, x, bottom))

		for y in range(first_top, bottom, self.GRID_SIZE):
			if y % (self.GRID_SIZE * self.GRID_SQUARE) != 0:
				light_lines.append(QtCore.QLine(left, y, right, y))
			else:
				dark_lines.append(QtCore.QLine(left, y, right, y))

		# draw the lines
		painter.setPen(self.penLight)
		painter.drawLines(light_lines)

		painter.setPen(self.penDark)
		painter.drawLines(dark_lines)

	
