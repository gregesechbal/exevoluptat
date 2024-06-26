   import networkx as nx

   # Create an undirected graph
   graph = nx.Graph()
   graph.add_edges_from([('x', 'y'), ('y', 'z')])

   # Check if the graph is directed
   nx.is_directed(graph)  # Output: False
   