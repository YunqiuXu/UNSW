#!/usr/bin/env python
# [PASSED]
# Calculates the shortest journey between two towns specified as arguments
# Dijkstra


import sys


# Function : get_edge_list, generate all edges from input
# Edge type: [length, (v1, v2)] --> an edge connect v1 and v2
def get_edges():
    edges = []
    for curr_line in sys.stdin.readlines():
        splitted = curr_line.split(' ')
        splitted = filter(None, splitted)
        edges.append([int(splitted[2]), (splitted[0],splitted[1])])
    return edges


# Function : get all incident edges for vertex
def get_incident_edges(vertex, edges):
    incident_edges = []
    for edge in edges:
        if vertex in edge[1]:
            incident_edges.append(edge)
    return incident_edges


# Function : get all vertices in a dict
# Key : vertex_name
# Value : Distance from start_vertex, for start_vertex is 0, others are infinity
def get_vertices(edges, start_vertex):
    vertices = {}
    for edge in edges:
        v1 = edge[1][0]
        v2 = edge[1][1]
        if v1 not in vertices:
            vertices[v1] = float('inf')
        if v2 not in vertices:
            vertices[v2] = float('inf')
    vertices[start_vertex] = 0
    return vertices


# Function : remove_min() --> remove min vertex
# return : min_vertex, remain_vertices
def remove_min(vertices):
    sorted_vertices = sorted(vertices.items(), key=lambda x:x[1])
    return sorted_vertices[0], dict(sorted_vertices[1:])


# Function : get_opposite(edge, vertex), get another vertex of an edge
def get_opposite(edge, vertex):
    for another in edge[1]:
        if another != vertex:
            return another 


# Function : Dijkstra
# Given a graph and start point, return
def dijkstraDistance(edges, start_vertex):

    # get vertices dict
    vertices = get_vertices(edges, start_vertex)
    path_dict = {} # store the path from start_vertex
    results = {} # store the shortest distances from start_vertex

    # init path dict
    for vertex in vertices.keys():
        path_dict[vertex] = []

    while len(vertices) != 0:
        curr_vertex, vertices = remove_min(vertices)
        curr_vertex_name = curr_vertex[0]
        curr_vertex_distance = curr_vertex[1]
        results[curr_vertex_name] = curr_vertex_distance
        # print "Current vertex is : " + str(curr_vertex)
        # print "After remove the vertices : " + str(vertices)

        new_path = path_dict[curr_vertex_name][:] # copy the list
        new_path.append(curr_vertex_name)
        for edge in get_incident_edges(curr_vertex_name, edges):

            # print "Current incident edge : " + str(edge)

            oppo_vertex = get_opposite(edge, curr_vertex_name)

            # print "Opposite vertex : " + str(oppo_vertex)

            # relaxation --> update the distance in heap
            if oppo_vertex in vertices:
                # print vertices[oppo_vertex]
                # print curr_vertex_distance + edge[0]
                
                if vertices[oppo_vertex] > curr_vertex_distance + edge[0]:
                    vertices[oppo_vertex] = curr_vertex_distance + edge[0]

                    # print "For vertex " + str(oppo_vertex)
                    # print "old path : " + str(path_dict[oppo_vertex])
                    path_dict[oppo_vertex] = new_path
                    # print "new path : " + str(path_dict[oppo_vertex])
                    # print "-----"

            # print "So the vertices : " + str(vertices)
            # print "And the results : " + str(results)
            # print "-----"

    return results, path_dict
    



if __name__ == "__main__":
    start_vertex = sys.argv[1]
    end_vertex = sys.argv[2]

    edges = get_edges()
    results, path_dict = dijkstraDistance(edges, start_vertex)

    shortest_dist = results[end_vertex]
    shortest_path = path_dict[end_vertex]
    shortest_path.append(end_vertex)

    print "Shortest route is length = {}: {}.".format(shortest_dist, ' '.join(shortest_path))


