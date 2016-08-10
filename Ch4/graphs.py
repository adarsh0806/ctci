graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['E'])}

# recursive approach
def dfs(graph, start, visited = None):
	if visited == None:
		visited = set()
	print 'start: ', start
	visited.add(start)
	for next in graph[start] - visited:
		# print 'graph[start]: ',graph[start]
		# print 'visited: ', visited
		# print 'graph[start] - visited: ', graph[start] - visited
		dfs(graph, next, visited)
		# print '\n'
	return visited
# print dfs(graph, 'A')

# non recursive
def dfs_nonrecursive(graph, start):
	visited = set()
	stack = [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

# print dfs_nonrecursive(graph, 'B')

# BFS non recursive approach: uses queues
def bfs_nonrecursive(graph, start):
	visited = set()
	queue = [start]
	while queue:
		# remove item at the front of the queue
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

print bfs_nonrecursive(graph, 'A')

# Paths
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# TODO
