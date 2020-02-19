from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # instantiate a graph
    graph = Graph()
    # loop through array of tuples
    for tuple in ancestors:
        # add numbers to set of possible vertices
        if tuple[0] not in graph.vertices:
            graph.add_vertex(tuple[0])
        if tuple[1] not in graph.vertices:
            graph.add_vertex(tuple[1])
    # Add edges from tuples BACKWARDS
    for tuple in ancestors:
        graph.add_edge(tuple[1], tuple[0])
    # print(graph.vertices)
    # find paths to every possible vertex using recursion
    path_list = []
    for vertex in graph.vertices:
        path = graph.dfs_recursive(starting_node, vertex)
        if path is not None:
            path_list.append(path)
    # print(path_list)
    # Create list of the lengths of possible paths
    lengths = []
    for path in path_list:
        lengths.append(len(path))
    # print(lengths)
    # Find the longest path
    for path in path_list:
        if len(path) is max(lengths):
            # Return -1 if only possible path is the same
            if path[-1] is starting_node:
                return(-1)
            else:
                # Append possible ends to array
                possible = []
                possible.append(path[-1])
                # Grab the least of possible ends.
                return min(possible)