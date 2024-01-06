import json
import numpy as np
from itertools import combinations
import sys
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

print(adj_matrix)

arr=adj_matrix
n=20
vertex=[]
for i in range(2,n+1):
    vertex.append(i)
dicts={}
for length in range(0,n):
    for j in combinations(vertex,length):
        for k in range(2,n+1):
            if k not in j:
                fs=frozenset(j)
                if len(j)==0:
                    dicts[(k,fs)]=[arr[k-1][0],1]
                else:
                    mini=sys.maxsize
                    v1=0
                    for m in j:
                        fs1=fs-frozenset([m])
                        temp=arr[k-1][m-1]+dicts[(m,fs1)][0]
                        if (mini>temp):
                            mini=temp
                            v1=m
                            dicts[(k,fs)]=(mini,v1)


print(dicts)
mini=sys.maxsize
v1=0
for i in vertex:
    fs=frozenset(vertex)-frozenset([i])
    temp=arr[0][i-1]+dicts[(i,fs)][0]
    if (mini>temp):
        mini=temp
        v1=i

dicts[(1,frozenset(vertex))]=(mini,v1)
path=[1]
remaining_places=frozenset(vertex)

print(dicts)

while len(remaining_places)!=0:
    a=dicts[(path[-1],remaining_places)][1]
    path.append(a)
    remaining_places=remaining_places-frozenset([a])

path.append(1)
print(path)
