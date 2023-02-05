from PySide6 import QtWidgets, QtCore, QtGui

TITLE_COLOR = QtCore.Qt.green
DEFAULT_COLOR = "#7F000000"
SELECTED_COLOR = "#FFFFA637"
TITILE_COLOR = "#FF313131"
BACKGROUND_COLOR = "#E3212121"

class GraphicsNode(QtWidgets.QGraphicsItem):
	def __init__(self, node, parent = None):
		super().__init__(parent)
		self.node = node 
		self.content = self.node.content

		# node setting
		self.width = 180
		self.height = 240
		self.edgeSize = 10.0
		self.titleHeight = 24.0
		self._padding = 4.0

		# set color
		self._pen_default = QtGui.QPen(QtGui.QColor(DEFAULT_COLOR))
		self._pen_selected = QtGui.QPen(QtGui.QColor(SELECTED_COLOR))

		self._brush_title = QtGui.QBrush(QtGui.QColor(TITILE_COLOR))
		self._brush_background = QtGui.QBrush(QtGui.QColor(BACKGROUND_COLOR))

		# init content
		self.init_title()
		self.title = self.node.title

		# init socket
		self.init_socket()

		# init content
		self.init_content()

		self.init_UI()

	def init_UI(self):
		self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
		self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

	def init_title(self):
		self.itemTitle = QtWidgets.QGraphicsTextItem(self)
		self.itemTitle.setDefaultTextColor(TITLE_COLOR)
		self.itemTitle.setPos(self._padding, 0)
		self.itemTitle.setTextWidth(self.width - 2 * self._padding)

	def boundingRect(self):
		return QtCore.QRectF(
				0, 
				0,
				self.width,
				self.height
			).normalized()

	@property
	def title(self):
		return self._title
	@title.setter
	def title(self, value):
		self._title = value
		self.itemTitle.setPlainText(self._title)

	def init_content(self):
		self.grContent = QtWidgets.QGraphicsProxyWidget(self)
		self.content.setGeometry(self.edgeSize, self.titleHeight + self.edgeSize, self.width - 2 * self.edgeSize, self.height - 2 * self.edgeSize - self.titleHeight)
		self.grContent.setWidget(self.content)

	def init_socket(self):
		pass


	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		# title
		path_title = QtGui.QPainterPath()
		path_title.setFillRule(QtCore.Qt.WindingFill)
		path_title.addRoundedRect(0,0, self.width, self.titleHeight, self.edgeSize, self.edgeSize)
		path_title.addRect(0, self.titleHeight - self.edgeSize, self.edgeSize, self.edgeSize)
		path_title.addRect(self.width - self.edgeSize, self.titleHeight - self.edgeSize, self.edgeSize, self.edgeSize)
		painter.setPen(QtCore.Qt.NoPen)
		painter.setBrush(self._brush_title)
		painter.drawPath(path_title.simplified())


		# content
		path_content = QtGui.QPainterPath()
		path_content.setFillRule(QtCore.Qt.WindingFill)
		path_content.addRoundedRect(0, self.titleHeight, self.width, self.height - self.titleHeight, self.edgeSize, self.edgeSize)
		path_content.addRect(0, self.titleHeight, self.edgeSize, self.edgeSize)
		path_content.addRect(self.width - self.edgeSize, self.titleHeight, self.edgeSize, self.edgeSize)
		painter.setPen(QtCore.Qt.NoPen)
		painter.setBrush(self._brush_background)
		painter.drawPath(path_content.simplified())


		# outline
		path_outline = QtGui.QPainterPath()
		path_outline.addRoundedRect(0, 0, self.width, self.height, self.edgeSize, self.edgeSize)
		painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
		painter.setBrush(QtCore.Qt.NoBrush)
		painter.drawPath(path_outline.simplified())

	# def paint(self, painter, QStyleOptionGraphicsItem, widget = None):
	# 	# title
	# 	path_title = QtGui.QPainterPath()
	# 	path_title.setFillRule(QtCore.Qt.WindingFill)
	# 	path_title.addRoundedRect(0, 0, self.width, self.titleHeight, self.edgeSize, self.edgeSize)
	# 	path_title.addRect(0, self.titleHeight - self.edgeSize, self.edgeSize, self.edgeSize)
	# 	path_title.addRect(self.width - self.edgeSize, self.titleHeight - self.edgeSize, self.edgeSize, self.edgeSize)
	# 	painter.setPen(QtCore.Qt.NoPen)
	# 	painter.setBrush(self._brush_title)
	# 	painter.drawPath(path_title.simplified())

	# 	# content
	# 	path_content = QtGui.QPainterPath()
	# 	path_content.setFillRule(QtCore.Qt.WindingFill)
	# 	path_content.addRoundedRect(0, self.titleHeight, self.width, self.height - self.titleHeight, self.edgeSize, self.edgeSize)
	# 	path_content.addRect(self.width - self.edgeSize, self.titleHeight, self.edgeSize, self.edgeSize)
	# 	painter.setPen(QtCore.Qt.NoPen)
	# 	painter.setBrush(self._brush_background)
	# 	painter.drawPath(path_content.simplified())

	# 	# outline
	# 	path_outline = QtGui.QPainterPath()
	# 	path_outline.addRoundedRect(0, 0, self.width, self.height, self.edgeSize, self.edgeSize)
	# 	painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
	# 	painter.setBrush(QtCore.Qt.NoBrush)
	# 	painter.drawPath(path_outline.simplified())


