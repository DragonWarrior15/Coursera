'''
submission for University of Caifornia Advanced Agorithms and Complexity
assignment 1 - network flows
submitted by Vaibhav Ojha
'''
'''
Input:
5 7
1 2 2
2 5 5
1 3 6
3 4 2
4 5 1
3 2 3
2 4 1
'''

from sys import stdin, stdout
from collections import deque

def get_augmenting_path(source, sink, no_of_vertices, matrix):
	'''
	get the path from source to sink with least no of edges
	'''
	print(matrix)
	
	return 0

# read the no of vertices and edges
no_of_vertices, no_of_edges = map( int, stdin.readline().rstrip().split() )

# initialize data storing matrices etc
capacity_matrix = [[0 for i in range(no_of_vertices)] for j in range(no_of_vertices)]
flows_matrix = [[0 for i in range(no_of_vertices)] for j in range(no_of_vertices)]

graph = {}
# read the edge details
for i in range(no_of_edges):
	start, end, capacity = map( int, stdin.readline().rstrip().split() )
	capacity_matrix[start][end] = capacity
	try:
		graph[start].add(end)
	except KeyError:
		graph[start] = set(end)

residual_matrix_flow = [[capacity_matrix[i][j] - flows_matrix[i][j] for j in range(no_of_vertices)] for i in range(no_of_vertices)]
residual_matrix_counter_flow = [[-flows_matrix[i][j] for j in range(no_of_vertices)] for i in range(no_of_vertices)]
source = 0
sink = no_of_vertices - 1


augmenting_path = get_augmenting_path(source, sink, no_of_vertices, residual_matrix_flow)