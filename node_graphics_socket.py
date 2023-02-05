from PySide6 import QtWidgets, QtGui, QtCore

BG_COLOR = "#FFFF7700"
OUTLINE_COLOR = "#FF000000"

class GraphicsSocket(QtWidgets.QGraphicsItem):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.radius = 6.0
		self.outlineWidth = 1.5
		self.bgColor = QtGui.QColor(BG_COLOR)
		self.outLineColor =	QtGui.QColor(OUTLINE_COLOR)

		self._pen = QtGui.QPen(self.outLineColor)
		self._pen.setWidthF(self.outlineWidth)
		self._brush = QtGui.QBrush(self.bgColor)

	def paint(self, paiter, QStyleOptionGraphicsItem, widget = None):
		# painting circle
		paiter.setBrush(self._brush)
		paiter.setPen(self._pen)
		paiter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

	def boundingRect(self):
		return QtCore.QRectF(
				-self.radius - self.outlineWidth,
				-self.radius - self.outlineWidth,
				2 * (self.radius + self.outlineWidth),
				2 * (self.radius + self.outlineWidth)
			)
