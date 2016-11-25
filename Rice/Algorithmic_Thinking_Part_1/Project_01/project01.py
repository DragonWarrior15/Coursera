'''
submission for rice university algorithmic thinking part 1
project 1 - degree distributions for graphs
submitted by Vaibhav Ojha
'''

# task 1, define graphs as dictionaries
# to be treated as global constants
EX_GRAPH0 = {
	0 : set([1, 2]),
	1 : set([]),
	2 : set([])
}

EX_GRAPH1 = {
	0 : set([1, 4, 5]),
	1 : set([2, 6]),
	2 : set([3]),
	3 : set([0]),
	4 : set([1]),
	5 : set([2]),
	6 : set([])
}

EX_GRAPH2 = {
	0 : set([1, 4, 5]),
	1 : set([2, 6]),
	2 : set([3, 7]),
	3 : set([7]),
	4 : set([1]),
	5 : set([2]),
	6 : set([]),
	7 : set([3]),
	8 : set([1, 2]),
	9 : set([0, 3, 4, 5, 6, 7])
}

def make_complete_graph(num_nodes):
	'''
	task 2, make a function that returns a 
	complete digraph, no node should have an edge to itself
	'''
	if num_nodes <= 0:
		return {}
	else:
		graph = {}
		for node in range(num_nodes):
			graph[node] = set([x for x in range(num_nodes) if x != node])
		return graph

def compute_in_degrees(digraph):
	'''
	task 3, make a function that takes a dictionary represented digraph
	as input and returns a dictionary of in degrees for all the nodes
	'''
	#num_nodes = len(digraph)
	#digraph_nodes = [key for key in digraph]
	in_degrees = {}
	for key in digraph:
		in_degree = 0
		for key1 in digraph:
			if key in digraph[key1]:
				in_degree += 1
		in_degrees[key] = in_degree
	return in_degrees

def in_degree_distribution(digraph):
	'''
	task 4, return the unnormalized distribution of the in_degrees
	as a dictionary
	'''
	in_degrees = compute_in_degrees(digraph)
	in_degrees_dist = {}
	for key in in_degrees:
		if in_degrees[key] not in in_degrees_dist:
			in_degrees_dist[in_degrees[key]] = 1
		else:
			in_degrees_dist[in_degrees[key]] += 1
	return in_degrees_dist

#print(len(EX_GRAPH1))
#print(compute_in_degrees(EX_GRAPH1))
#print(in_degree_distribution(EX_GRAPH2))