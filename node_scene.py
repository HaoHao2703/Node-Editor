from node_graphic_scene import GraphicScene

class Scene():
	def __init__(self):
		self.nodes = []
		self.edges = []

		self.scene_width = 64000
		self.scene_height = 64000

		self.init_UI()

	def init_UI(self):
		self.grScene = GraphicScene(self)
		self.grScene.set_graphic_scene(self.scene_width, self.scene_height)



	def addNode(self, node):
		self.nodes.append(node)

	def addEdge(self, edge):
		self.edges.append(edge)

	def removeNode(self, node):
		self.nodes.remove(node)

	def removeEdge(self, node):
		self.edges.remove(edge)