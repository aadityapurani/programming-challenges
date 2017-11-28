#!/usr/bin/python

'''
DFS (Depth First Search) works on Stack Concept, let's say you want to go from Node A to Node D, then first put A in stack, try to visit it's adjacent unvisited node according to the priority you set (like alphabetical order) then mark it as visited and continue same until you finish traversal
'''

edges = {
'S': ['A', 'B', 'C'],
'A': ['D', 'S'],
'D': ['A', 'B', 'C'],
'B': ['D', 'S'],
'C': ['D', 'S']
}


def dfs(edges, f, l, slist=[]):
	if f == l:
		return [f]
	if f not in edges:
		return []
	slist.append(f)
	for x in edges[f]:
		if x in slist: continue
		res = dfs(edges, x, l, slist)
		if (res):
			way = [f]
			way.extend(res)
			return way
	return []




way = dfs(edges, 'S', 'D')
if way:
	print ', '.join(map(str,way))
else:
	print 'Not Possible'
