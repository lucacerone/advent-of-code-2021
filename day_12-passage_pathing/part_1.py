import utils as u

graph = u.import_graph("./data/input")
connections = u.to_connections(graph)



n_paths = u.count_paths("start", connections)

print(f"There are {n_paths} paths through this cave system that visit small caves at most once.")
