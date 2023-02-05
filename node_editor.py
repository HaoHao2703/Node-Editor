from PySide6 import QtWidgets, QtCore
import sys

from node_graphic_view import GraphicsView
from node_scene import Scene
from node_node import Node



class NodeEdiorWin(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.stylesheetFilename = "qss/nodestyle.qss"
		self.load_style_sheet(self.stylesheetFilename)
		self.init_UI()

	def init_UI(self):
		self.setGeometry(200, 200, 800, 600)

		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.layout)

		# create graphics scene
		self.scene = Scene()
		# self.grScene = self.scene.grScene

		node = Node(self.scene, "My Node", inputs = [1, 2, 3], outputs = [1])

		# create graphics view
		self.view = GraphicsView(self.scene.grScene, self)
		# self.view.setScene(self.grScene)
		self.layout.addWidget(self.view)


		self.setWindowTitle("Hao's Editor")
		# self.addDebugContent()

		self.show()

	def load_style_sheet(self, filename):
		print("Style loading: ", filename)
		file = QtCore.QFile(filename)
		file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text )
		styleSheet = file.readAll()
		QtWidgets.QApplication.instance().setStyleSheet(str(styleSheet, encoding = 'utf-8'))

	def addDebugContent(self):
		greenBrush = QtGui.QBrush(QtCore.Qt.green)
		outlinePen = QtGui.QPen(QtCore.Qt.black)
		outlinePen.setWidth(2)

		rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
		rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

		widget2 = QtWidgets.QTextEdit()
		proxy2 = self.grScene.addWidget(widget2)
		proxy2.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
		proxy2.setPos(0, 60)

		line = self.grScene.addLine(-200, -200, 400, -100, outlinePen)
		line.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
		line.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
		

def main():
	app = QtWidgets.QApplication(sys.argv)

	win = NodeEdiorWin()
	win.show()

	app.exec_()

# main()
