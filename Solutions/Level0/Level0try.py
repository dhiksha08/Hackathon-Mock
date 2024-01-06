import json
import numpy as np

def minimum_spanning_tree(graph,start_node):
    n = len(graph)
    visited = [False] * n
    edges = []
    visited[start_node] = True

    while len(edges) < n - 1:
        min_edge = None
        min_weight = float('inf')

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] < min_weight:
                        min_edge = (i, j)
                        min_weight = graph[i][j]

        if min_edge:
            edges.append(min_edge)
            visited[min_edge[1]] = True

    return edges

def twice_around_the_tree(graph, start_node):
    n = len(graph)
    
    # Step 1: Find Minimum Spanning Tree
    mst_edges = minimum_spanning_tree(graph,start_node)
    
    # Step 2: Form a tour by traversing MST twice
    tour = []
    for edge in mst_edges:
        tour.extend(edge)

    # Step 3: Remove repeated vertices to obtain a Hamiltonian cycle
    hamiltonian_cycle = list(dict.fromkeys(tour))

    # Step 4: Ensure the cycle returns to the starting node
    hamiltonian_cycle.append(start_node)

    # Step 5: Calculate the cost of the Hamiltonian cycle
    hamiltonian_cost = sum(graph[hamiltonian_cycle[i]][hamiltonian_cycle[i + 1]] for i in range(len(hamiltonian_cycle) - 1))

    return hamiltonian_cycle, hamiltonian_cost

# Load data from JSON
with open('Student Handout\Input data\level0.json', 'r') as file:
    data = json.load(file)


# Create an adjacency matrix
n = data["n_neighbourhoods"] + 1  # Include the restaurant
adj_matrix = np.zeros((n, n))

# Fill the adjacency matrix with distances between neighborhoods
for i in range(data["n_neighbourhoods"]):
    for j, distance in enumerate(data["neighbourhoods"][f"n{i}"]["distances"]):
        adj_matrix[i][j] = distance

# Fill the adjacency matrix with distances between the restaurant and neighborhoods
restaurant_neighborhood_distances = data["restaurants"]["r0"]["neighbourhood_distance"]
for i, distance in enumerate(restaurant_neighborhood_distances):
    adj_matrix[n - 1][i] = distance
    adj_matrix[i][n - 1] = distance

# Set starting node (restaurant)
start_node = n - 1

# Apply the heuristic
hamiltonian_cycle, hamiltonian_cost = twice_around_the_tree(adj_matrix, start_node)

# Print results
print("Hamiltonian Cycle:", hamiltonian_cycle)
print("Hamiltonian Cost:", hamiltonian_cost)
print(len(hamiltonian_cycle))
print(hamiltonian_cycle)
res=[]
for i in hamiltonian_cycle:
    if (i==n-1):
        res.append("r0")
    else:
        res.append("n"+str(i))
print(res)

result_json = {"v0": {"path":res}}

print(result_json)
file_path = 'Solutions\level0_output.json'

# Write the JSON structure to the file
with open(file_path, 'w') as json_file:
    json.dump(result_json, json_file, indent=2)
