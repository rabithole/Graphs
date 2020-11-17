from util import Stack, Queue
from collections import deque
from graph import Graph
from collections import defaultdict	

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
	queue = deque()
	queue.append(starting_node)
	relationship = {}
	temp = {} 
	for ancestor in ancestors:
		if ancestor[1] in relationship: 
			temp = ancestor[]
			relationship[ancestor[1]] = {temp, ancestor[0]} 
			temp = ancestor[0] 
			print('Child', ancestor[1], 'Temp', temp, 'Parent', ancestor[0])
		else: 
			relationship[ancestor[1]] = {ancestor[0]} 
			# temp = ancestor[0] 
	print(relationship)


	
	

# print('Targeted', ancestors[8])
print('')
print('Ancestor', earliest_ancestor(ancestors, 9))
print('')
# Earliest known ancestor will have the longest path
# If more than one ancestor, return the one with the lowest numberic ID/value.
# Return -1 if there no parents exist. 

def createGraph(edges):
    # This convenience method simply allows us to initialize default values when assigning
    # a key to a dictionary. In this case, the default value for a new key is an empty set
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    print(graph)
    return graph

createGraph(ancestors)




def earliest_ancestor1(ancestors, starting_node):
    queue = Queue()
    current_node = starting_node
    relationships = {}

    for ancestor in ancestors:
        parent = ancestor[0]	
        child = ancestor[1]

        if child not in relationships:
            relationships[child] = set()
        relationships[child].add(parent)
    print(relationships)

# earliest_ancestor1(ancestors, 6)