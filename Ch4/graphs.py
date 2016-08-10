graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['E'])}

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

print dfs(graph, 'A')

