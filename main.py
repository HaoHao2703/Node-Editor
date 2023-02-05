import sys
from PySide6.QtWidgets import *
from node_editor import *

if __name__ == "__main__":
	app = QApplication(sys.argv)

	win = NodeEdiorWin()
	# win.show()

	sys.exit(app.exec())
	




