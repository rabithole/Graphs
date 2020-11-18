from util import Stack, Queue
from collections import deque
from graph import Graph
from collections import defaultdict	

# ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


# def earliest_ancestor(ancestors, starting_node):
# 	queue = deque()
# 	queue.append(starting_node)
# 	relationship = {}
	
# 	for ancestor in ancestors: 
# 		parent, child = ancestor[0], ancestor[1] # Sets 0 and 1 index to respective parent and child variables.

# 		if child not in relationship: # If 1 index not in the relationshop dictionary, relationship key is the child/0 index.
# 			relationship[child] = set() # This sets the dictionary value to an empty set().
# 		relationship[child].add(parent) # Adds the parent index 0 to the dictionary value
		
# 	print('Myne', relationship)


	
	

# # print('Targeted', ancestors[8])
# print('')
# print('Ancestor', earliest_ancestor(ancestors, 9))
# print('')
# # Earliest known ancestor will have the longest path
# # If more than one ancestor, return the one with the lowest numberic ID/value.
# # Return -1 if there no parents exist. 


def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    # A tuple with a node and its distance from the starting node
    # At the beginning, the starting node's earliest ancestor is itself
    earliestAncestor = (starting_node, 0)
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        # This checks if the node is a terminal node
        if currNode not in graph:
        # Only consider terminal nodes that have a greater distance than the ones we've found so far
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            # If there's a tie then choose the ancestor with the lower id
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    # If the starting node's earliest ancestor is itself, then just return -1
    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

# Creates a graph where the keys are a node and its values are its ancestors
def createGraph(edges):
    # This convenience method simply allows us to initialize default values when assigning
    # a key to a dictionary. In this case, the default value for a new key is an empty set
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph[child] = set()
        relationships[child].add(parent)
    print(relationships)