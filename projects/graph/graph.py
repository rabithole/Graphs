from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # vertex_id = key / set() = the value
        self.vertices[vertex_id] = set()

    def add_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Can not add an edge to a non-existent node!")
            return 
        self.vertices[from_vertex_id].add(to_vertex_id)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        visited = set()
        queue = deque()
        # print('queue', queue)
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print('BFT', currNode)
                for neighbor in self.vertices[currNode]:
                    print(neighbor)
                    queue.append(neighbor)
        

    def dft(self, starting_vertex):
        visited =set()
        stack = deque()
        # print('stack', type(stack))
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print('DFT', currNode)
                for neighbor in self.vertices[currNode]:
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        self.dft_recursive_helper(starting_vertex, visited)

    def dft_recursive_helper(self, curr_vertex, visited):
        visited.add(curr_vertex)
        print(curr_vertex)
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                self.dft_recursive_helper(neighbor, visited)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = deque()
        queue.append([starting_vertex])
        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.append(newPath)
        return []

    def dfs(self, starting_vertex, gaol_vertex):
        visited = set()
        stack = deque()
        # Push the current path your're on onto the stack, instead of just a single vertex.
        stack.append([starting_vertex])
        while len(stack) > 0:
            currPath = stack.pop()
            currNode = currPath[-1] # the current node you're on is the last node in the pa
            if currNode == gaol_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath) # make a copy of the current path
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        visited = set()
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, visited)

    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        curr_vertex = curr_path[-1]
        if curr_vertex == destination_vertex:
            return curr_path
        visited.add(curr_vertex)
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                newPath = list(curr_path)
                newPath.append(neighbor)
                res = self.dfs_recursive_helper(newPath, destination_vertex, visited)
                if len(res) > 0:
                    return res
        return []

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)



    '''
    Should print:
        {
            1: {2}, 
            2: {3, 4}, 
            3: {5}, 
            4: {6, 7}, 
            5: {3}, 
            6: {3}, 
            7: {1, 6}
        }
    '''
    print('')
    print('Graph Vertices: --------------', graph.vertices[2])
    print('Graph Vertices: --------------', graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print('')

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('Graph bfs: ----------', graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('Graph dfs: -----------', graph.dfs(1, 6))
    print('Graph dfs recursive: ----------------', graph.dfs_recursive(1, 6))
    print('')