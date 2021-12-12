import utils as u

graph = u.import_graph("./data/input")
connections = u.to_connections(graph)

print(connections)

# paths = u.find_paths("start", connections)

#n_paths = len(paths)

#print(f"There are {n_paths} paths through this cave system that visit small caves at most once.")
