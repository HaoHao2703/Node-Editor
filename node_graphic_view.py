from PySide6 import QtWidgets, QtCore, QtGui

class GraphicsView(QtWidgets.QGraphicsView):
	def __init__(self, grScene, parent = None):
		super().__init__(parent)

		self.grScene = grScene
		self.init_UI()
		self.setScene(self.grScene)

		self.zoomInFactor = 1.25
		self.zoom = 10
		self.zoomStep = 1
		self.zoomRange = [0, 10]
		self.zoomClamp = False

	def init_UI(self):
		self.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing | QtGui.QPainter.SmoothPixmapTransform)

		self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)

		self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

		self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.MiddleButton:
			self.middleMouseButtonPress(event)
		elif event.button() == QtCore.Qt.LeftButton:
			self.leftMouseButtonPress(event)
		elif event.button() == QtCore.Qt.RightButton:
			self.rightMouseButtonPress(event)
		else:
			super().mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		if event.button() == QtCore.Qt.MiddleButton:
			self.middleMouseButtonRelease(event)
		elif event.button() == QtCore.Qt.LeftButton:
			self.leftMouseButtonRelease(event)
		elif event.button() == QtCore.Qt.RightButton:
			self.rightMouseButtonRelease(event)
		else:
			super().mouseReleaseEvent(event)

	# drag window
	def middleMouseButtonPress(self, event):
		releaseEvent = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, event.localPos(), event.screenPos(), QtCore.Qt.LeftButton, QtCore.Qt.NoButton, event.modifiers())
		super().mouseReleaseEvent(releaseEvent)
		self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
		dragEvent = QtGui.QMouseEvent(event.type(), event.localPos(), event.screenPos(), QtCore.Qt.LeftButton, event.buttons() | QtCore.Qt.LeftButton, event.modifiers())
		super().mousePressEvent(dragEvent)

	def middleMouseButtonRelease(self, event):
		dragEvent = QtGui.QMouseEvent(event.type(), event.localPos(), event.screenPos(), QtCore.Qt.LeftButton, event.buttons() & ~QtCore.Qt.LeftButton, event.modifiers())
		super().mouseReleaseEvent(dragEvent)
		self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

	def leftMouseButtonPress(self, event):
		return super().mousePressEvent(event)

	def leftMouseButtonRelease(self, event):
		return super().mouseReleaseEvent(event)

	def rightMouseButtonPress(self, event):
		return super().mouseReleaseEvent(event)

	def rightMouseButtonRelease(self, event):
		return super().mouseReleaseEvent(event)

	def wheelEvent(self, event):
		# calculate zoom factor
		zoomOutFactor = 1 / self.zoomInFactor

		# calculate zoom
		if event.angleDelta().y() > 0:
			zoomFactor = self.zoomInFactor
			self.zoom += self.zoomStep
		else:
			zoomFactor = zoomOutFactor
			self.zoom -= self.zoomStep

		# set scene scale
		self.scale(zoomFactor, zoomFactor)



