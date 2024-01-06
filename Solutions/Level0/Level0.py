import json
import pandas as pd
import networkx as nx
import numpy as np

with open('Student Handout\Input data\level0.json', 'r') as file:
    data = json.load(file)

# Create an adjacency matrix
adj_matrix = [[float('inf')] * (data["n_neighbourhoods"] + 1) for _ in range(data["n_neighbourhoods"] + 1)]

# Fill the adjacency matrix with distances between the restaurant and neighborhoods
restaurant_neighborhood_distances = data["restaurants"]["r0"]["neighbourhood_distance"]
for i, distance in enumerate(restaurant_neighborhood_distances):
    adj_matrix[data["n_neighbourhoods"]][i] = distance
    adj_matrix[i][data["n_neighbourhoods"]] = distance

# Fill the adjacency matrix with distances between neighborhoods
for i in range(data["n_neighbourhoods"]):
    for j, distance in enumerate(data["neighbourhoods"][f"n{i}"]["distances"]):
        adj_matrix[i][j] = distance

tsp_g = adj_matrix
adj_matrix[data["n_neighbourhoods"]][data["n_neighbourhoods"]]=0
visited = [0] * (data["n_neighbourhoods"]+1)
n = data["n_neighbourhoods"]+1
cost = 0
path=[]
def travellingsalesman(c):
    global cost
    adj_vertex = 999
    min_val = 999
    visited[c] = 1
    path.append(c)
    for k in range(n):
        if (tsp_g[c][k] != 0 and visited[k] == 0):
            if (tsp_g[c][k] < min_val):
                min_val = tsp_g[c][k]
                adj_vertex = k
    if (min_val != 999):
        cost = cost + min_val
    if (adj_vertex == 999):
        adj_vertex = 0

        path.append(adj_vertex)
        cost += tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)

print("Shortest Path: ", end = " ")
travellingsalesman(0)
print("\nMinimum Cost: ", cost)
print(path)
path.remove(20)
print(path)
final=[0]*(len(path))
for i in range(len(path)):
    if (i!=0 and i!=len(path)-1):
        final[i]="n"+str(path[i])
    else:
        final[i]="r0"
final.insert(1,"n0")
print(final)

result_json = {"v0": {"path":final}}

print(result_json)
file_path = 'Solutions\level0_output.json'

# Write the JSON structure to the file
with open(file_path, 'w') as json_file:
    json.dump(result_json, json_file, indent=2)
