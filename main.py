class Node:
	def __init__(self, owner, id = 0):
		self.owner = owner
		self.id = id
		self.children = None
	
	def set_children(self, children):
		self.children = children
			
	def access_owner(self):
		return self.owner.id

	def access_child(self, id):
		return self.children[id]


def set_net():
	core = Node(None, 0)
	agregation = [Node(core, 0), Node(core, 1)]
	core.set_children(agregation)

	edge = [Node(agregation[0], 0), Node(agregation[0], 1), Node(agregation[1], 2), Node(agregation[1], 3)]
	agregation[0].set_children(edge[0:2])
	agregation[1].set_children(edge[2:4])

	hosts_from_0 = [Node(edge[0], i) for i in range(24)]
	edge[0].set_children(hosts_from_0)
	hosts_from_1 = [Node(edge[1], i) for i in range(24)]
	edge[1].set_children(hosts_from_1)
	hosts_from_2 = [Node(edge[2], i) for i in range(15)]
	edge[2].set_children(hosts_from_2)
	hosts_from_3 = [Node(edge[3], i) for i in range(15)]
	edge[3].set_children(hosts_from_3)

	return core


def rec_search(net, id_list = [], level = 0, flag = False):
	#This code is untested and not optimized
	if net.owner == None:
		new = net.access_child(id_list[level])
		rec_search(new, id_list, level + 1, True)
	else:
		if flag:
			if net.children == None:
				return net.id
			else:
				new = net.access_child(id_list[level])
				rec_search(new, id_list, level + 1, True)
			pass
		else:
			new = net.access_owner(id_list[level])
			rec_search(new, id_list, level + 1, False)

	pass


def main():
	#  Kinda scuffed for now but... nhe
	net_core = set_net()
	rec_search(net_core, [0, 0, 15])
	print(net_core.children)


if __name__ == "__main__":
	main()
