'''
submission for rice university algorithmic thinking part 1
project 2 - connected components and graph resilience
submitted by Vaibhav Ojha
'''
from collections import deque

def bfs_visited(ugraph, start_node):
	'''
	Takes the undirected graph ugraph and the node start_node and returns the set 
	consisting of all nodes that are visited by a breadth-first search that 
	starts at start_node.
	'''
	visited = []
	neighbour_queue = deque()
	visited.append(start_node)
	neighbour_queue.append(start_node)
	while len(neighbour_queue) > 0:
		next_node = neighbour_queue.pop()
		for node in ugraph[next_node]:
			if node not in visited:
				visited.append(node)
				neighbour_queue.append(node)
	
	return set(visited)

def cc_visited(ugraph):
	'''
	Takes the undirected graph ugraph and returns a list of sets, 
	where each set consists of all the nodes (and nothing else) in a connected 
	component, and there is exactly one set in the list for each connected 
	component in ugraph and nothing else.
	'''
	connected_set = []
	remaining_nodes = set([node for node in ugraph])
	while len(remaining_nodes) > 0:
		next_node = remaining_nodes.pop()
		remaining_nodes.add(next_node)
		connected_set_this_node = bfs_visited(ugraph, next_node)
		connected_set.append(connected_set_this_node)
		remaining_nodes = remaining_nodes.difference(connected_set_this_node)

	return connected_set

def largest_cc_size(ugraph):
	'''
	Takes the undirected graph ugraph and returns the size (an integer) 
	of the largest connected component in ugraph.
	'''
	connected_sets = cc_visited(ugraph)
	size_list = [len(connected_set) for connected_set in connected_sets]
	print(size_list, ugraph)
	return max(size_list)

def compute_resilience(ugraph, attack_order):
	'''
	Takes the undirected graph ugraph, a list of nodes attack_order and iterates 
	through the nodes in attack_order. For each node in the list, the function 
	removes the given node and its edges from the graph and then computes the 
	size of the largest connected component for the resulting graph. The function 
	should return a list whose k+1th entry is the size of the largest connected component 
	in the graph after the removal of the first k nodes in attack_order. 
	The first entry (indexed by zero) is the size of the largest connected component 
	in the original graph.
	'''
	return_size_list = [largest_cc_size(ugraph)]
	for attacked_node in attack_order:
		ugraph.pop(attacked_node)
		if len(ugraph) == 0:
			return_size_list.append(0)
		else:
			for node in ugraph:
				if attacked_node in ugraph[node]:
					ugraph[node] = set(ugraph[node]).difference([attacked_node])
			return_size_list.append(largest_cc_size(ugraph))

	return return_size_list

#GRAPH2 = {1: set([2, 4, 6, 8]),
#          2: set([1, 3, 5, 7]),
#          3: set([2, 4, 6, 8]),
#          4: set([1, 3, 5, 7]),
#          5: set([2, 4, 6, 8]),
#          6: set([1, 3, 5, 7]),
#          7: set([2, 4, 6, 8]),
#          8: set([1, 3, 5, 7])}

#print(bfs_visited(GRAPH4, 0))
#print(cc_visited(GRAPH4))
#print(compute_resilience(GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8]))