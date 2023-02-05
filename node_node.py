from node_graphic_node import GraphicsNode
from node_content_widget import NodeContentWidget
from node_socket import *

class Node():
	def __init__(self, scene, title = "Undefined Node", inputs = [], outputs = []):
		# super().__init__(self)
		self.scene = scene
		self.title = title

		self.content = NodeContentWidget()
		self.grNode = GraphicsNode(self)

		self.scene.addNode(self)
		self.scene.grScene.addItem(self.grNode)

		self.socketSpacing = 22
		self.inputs = []
		self.outputs = []

		counter = 0
		for item in inputs:
			socket = Socket(node = self, index = counter, position = LEFT_BOTTOM)
			counter += 1
			self.inputs.append(socket)

		counter = 0
		for item in outputs:
			socket = Socket(node = self, index = counter, position = RIGHT_BOTTOM)
			counter += 1
			self.outputs.append(socket)

	def get_socket_pos(self, index, position):
		x = 0 if (position in (LEFT_TOP, LEFT_BOTTOM)) else self.grNode.width

		if position in (LEFT_BOTTOM, RIGHT_BOTTOM):
			# start from bottom
			y = self.grNode.height - self.grNode.edgeSize - self.grNode._padding - index * self.socketSpacing
		else:
			# start from top
			y = self.grNode.title_height + self.grNode._padding + self.grNode.edgeSize + index * self.socketSpacing
		return x, y