import random

def contract(graph):
    while len(graph) > 2:
        # Choose a random edge
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        
        # Merge vertices u and v
        graph[u].extend(graph[v])
        for vertex in graph[v]:
            graph[vertex].remove(v)
            graph[vertex].append(u)
        
        # Remove self-loops
        graph[u] = [x for x in graph[u] if x != u]
        
        del graph[v]

    # Return the remaining edges, which represent the cut
    remaining_edges = len(list(graph.values())[0])
    return remaining_edges

def min_cut(graph, num_trials):
    min_cut = float('inf')
    for _ in range(num_trials):
        graph_copy = {key: value[:] for key, value in graph.items()}
        cut = contract(graph_copy)
        min_cut = min(min_cut, cut)
    return min_cut

def read_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = [int(x) for x in line.strip().split()]
            graph[parts[0]] = parts[1:]
    return graph

if __name__ == "__main__":
    filename = "karger_min_cut.txt"  # Replace with the name of your input file
    graph = read_graph(filename)
    num_trials = 200  # Number of trials to run the algorithm
    
    min_cut_result = min_cut(graph, num_trials)
    print("Minimum cut found:", min_cut_result)