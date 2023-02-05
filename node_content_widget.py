from PySide6 import QtWidgets

class NodeContentWidget(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.init_UI()

	def init_UI(self):
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.layout)

		self.widget_label = QtWidgets.QLabel("Node")
		self.layout.addWidget(self.widget_label)
		self.layout.addWidget(QtWidgets.QTextEdit("foo"))

		