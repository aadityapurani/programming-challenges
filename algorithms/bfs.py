#!/usr/bin/python
'''
Breadth first search
It is used to find shortest path of unweighted graph
'''
graph = {
'A' : ['B', 'E', 'C'],
'B' : ['D', 'E', 'A'],
'C' : ['A', 'F', 'G'],
'D' : ['B'],
'E' : ['A', 'B','D'],
'F' : ['C'],
'G' : ['C']
}

def bfs_connected_components(graph, start):
	explored = []
	queue = [start]

	while queue:
		node = queue.pop(0)
		if node not in explored:
			explored.append(node)
			neighbours = graph[node]
			
			for neighbour in neighbours:
				queue.append(neighbour)
	return explored



def bfs_shortest_path(graph, start, goal):
	explored = []
	queue = [start]

	if start == goal:
		return "Found"

	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node not in explored:
			neighbours = graph[node]
			for n in neighbours:
				new_path = list(path)
				new_path.append(n)
				queue.append(new_path)
				if n == goal:
					return new_path
			explored.append(node)
	return "Doesn't exist"

print bfs_shortest_path(graph, 'G','D')

print bfs_connected_components(graph, 'A')
