"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """           
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue, add starting vertex id to queue
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # check if it's been visited
            # if it has not been visited
            if v not in visited:
                # Mark it as visited 
                print(v)
                visited.add(v)
                # Then add all the neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
        
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack, 
        # add/push starting vertex id to stack
        s = Stack()
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Dequeue/pop the first vertex
            v = s.pop()
            # check if it's been visited
            # if it has not been visited
            if v not in visited:
                # Mark it as visited 
                print(v)
                visited.add(v)
                # Then add all the neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # HINT: https://docs.python-guide.org/writing/gotchas/
        # hint: default args may help
        # Check if the node is visited
        # if not 
            # mark it as visited
            # print
            # Call dft(recursive) on each neighbor
        if visited is None:
            visited = set()
        # mark it as visited
        print('dft_recursive', starting_vertex)
        visited.add(starting_vertex)
        # Call dft_recursive on each neighbor not in visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # example
        #destination_vertex = 6
        # keep checking last number in first []
        # q = [  [1,2,3,5]  [1,2,4,6], [1,2,4,7]]
        # visited = { 1,2,3,4}
        # take the first [] in the list, go through it, then add neighbor, then addd new [] to back of queue
        # [1,2,3,5]
        
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            v = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            if v[-1] == destination_vertex:
                return v
            # CHECK IF IT'S THE TARGET
            if v[-1] not in visited:
                # IF SO, RETURN THE PATH
                path = []
                # If it has not been visited...
                for item in v:
                # Mark it as visited
                    path.append(item)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v[-1]):
                # (Make a copy of the path before adding)
                    q.enqueue(path + [neighbor])
        



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack
        s = Stack()
        # Add A PATH TO the starting vertex_id to the queue
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # pop, the first PATH
            v = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            # CHECK IF IT'S THE TARGET
            if v[-1] == destination_vertex:
                # IF SO, RETURN THE PATH
                return v
            # Check if it's been visited
            if v[-1] not in visited:
                # IF SO, RETURN THE PATH
                path = []
                # Mark it as visited
                # Then add A PATH TO all neighbors to the back of the stack
                # (Make a copy of the path before adding)
                for item in v:
                    path.append(item)
                for neighbor in self.get_neighbors(v[-1]):
                    s.push(path + [neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print('dfs_recursive', starting_vertex)
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        # Call dfs_recursive on each neighbor not in visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                #print(neighbor, destination_vertex, visited, path)
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path

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
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

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
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
