import networkx as nx

class Generic_Node:
	size=0
	def __init__(self, name):
		self.id = str(Generic_Node.size) + "_" + name
		Generic_Node.size += 1

	def __repr__(self):
		return self.id

class Arbitrator_Node(Generic_Node):
	def __init__(self, name, sen, total_cases):
		super().__init__("Arbitrator_"+name)
		self.seniority = sen
		self.total_cases = total_cases

class Case_Node(Generic_Node):

	Accepted_Case_Natures = ["construction"]

	def __init__(self, nature, amount):

		if nature not in Case_Node.Accepted_Case_Natures:
			raise ValueError(nature, "must be one of", Case_Node.Accepted_Case_Natures)
		super().__init__("Case_"+nature)
		self.dispute_amount = amount


a1 = Arbitrator_Node("saad", 1, 1)
c1 = Case_Node("construction", 1000)
c2 = Case_Node("construction", 500)


G = nx.DiGraph()
G.add_node(a1)
G.add_node(c1)
G.add_node(c2)

G.add_node('s')
G.add_node('t')

print(G.nodes)
 
G.add_edge('s', c1, capacity=1)
G.add_edge('s', c2, capacity=1)
G.add_edge(c1, a1, capacity=0.5)
G.add_edge(c2, a1, capacity=0.2)
G.add_edge(a1, 't', capacity=1)

v, d = nx.maximum_flow(G, 's', 't')
print(v)
print(d)







