from collections import deque
from heapq import heappush, heappop 
import math

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

    def ssp_recursive(past_nodes, frontier):
        
        if len(frontier) == 0:
            return past_nodes
        
        else:
            distance, node_edges = heappop(frontier)
            node = node_edges[0]
            edges = node_edges[1]

            if node in past_nodes:
                if past_nodes[node][0] == distance:
                    if past_nodes[node][1] > edges:
                      past_nodes[node] = (distance, edges)
                return ssp_recursive(past_nodes, frontier)
            
            else:
                past_nodes[node] = (distance, edges) 
                for adjacent_node, weight in graph[node]:
                    heappush(frontier, (distance + weight, (adjacent_node, edges + 1)))
                return ssp_recursive(past_nodes,frontier)

    frontier = []
    heappush(frontier, (0, (source, 0)))
    past_nodes = dict()
    return ssp_recursive(past_nodes, frontier)
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    def bp_recursive(past_nodes, frontier, path):
        if len(frontier) == 0:
            return path
        
        else:
            tmp = set()

            for node in frontier:
                past_nodes.add(node)

                for adjacent_node in graph[node]:
                    if adjacent_node in past_nodes:
                        pass
                    elif adjacent_node in frontier:
                        pass
                    
                    else:
                        path[adjacent_node] = node
                        tmp.add(adjacent_node)

            frontier = tmp
            return bp_recursive(past_nodes, frontier, path)
        
    past_nodes = set()
    frontier = set([source])
    path = dict()
    return bp_recursive(past_nodes, frontier, path)

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    def gp_recursive(parents, destination, path):

        if parents[destination] == 's':
            path.append('s')
            return path
        
        else:
            path.append(parents[destination])
            return gp_recursive(parents, parents[destination], path)
            
    path = [destination]
    path = gp_recursive(parents, destination, path)

    strres = ''
    i = 0
    while i < len(path) - 1:
        strres += path[len(path) - i - 1]
        i += 1

    return strres
