import json
import numpy as np
import pandas as pd

def nearest_neighbourhood(graph, start_node):
    n = len(graph)
    visited = [False] * n
    tour = [start_node]
    current_node = start_node

    for _ in range(n - 1):
        min_distance = float('inf')
        next_node = None

        for neighbor in range(n):
            if not visited[neighbor] and graph[current_node][neighbor] < min_distance and neighbor != start_node:
                min_distance = graph[current_node][neighbor]
                next_node = neighbor

        if next_node is not None:
            tour.append(next_node)
            visited[next_node] = True
            current_node = next_node

    return tour

def calculate_tour_cost(graph, tour):
    tour_cost = sum(graph[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return tour_cost

# Load data from JSON
with open('Student Handout\Input data\level1a.json', 'r') as file:
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

# Set the desired starting and ending node (e.g., node 20)
start_end_node = 20

# Apply the nearest neighborhood heuristic
nnh_tour = nearest_neighbourhood(adj_matrix, start_end_node)

# Ensure the tour starts and ends at the specified node
nnh_tour.append(start_end_node)

# Calculate the cost of the NNH tour
nnh_tour_cost = calculate_tour_cost(adj_matrix, nnh_tour)


# Assuming your data is stored in a variable named 'data'
neighbourhoods_data = data["neighbourhoods"]


qty=[]
# Extracting neighborhood names and order quantities
for neighbourhood, details in neighbourhoods_data.items():
    name = neighbourhood
    order_quantity = details["order_quantity"]
    qty.append(order_quantity)


total_capacity=data["vehicles"]["v0"]["capacity"]


division=[]

#taken from level0
route=nnh_tour
route=route[1:len(route)-1]
paths=[]
path=[]
cap=0
for i in route:
    if (cap+qty[i]<=600):
        cap=cap+qty[i]
    else:
        paths.append(path)
        path=[]
        cap=qty[i]
    path.append(i)
paths.append(path)
count=0
dict={}
for path in paths:
    temp=["r0"]
    for j in path:
        temp.append("n"+str(j))
    temp.append("r0")
    count+=1
    dict["path"+str(count)]=temp

tempy={"v0":dict}
print(tempy)
file_path = 'Solutions\Output\level1a_output.json'

# Write the JSON structure to the file
with open(file_path, 'w') as json_file:
    json.dump(tempy, json_file, indent=2)