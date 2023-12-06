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
        print('top')
        print(past_nodes)
        print(frontier)
        print(path)

        if len(frontier) == 0:
            return path
        
        else:
            past_nodes = past_nodes or frontier
            tmp = set()
            for node in frontier:
                for adjacent_node in graph[node[0]]:
                    
                    if adjacent_node in past_nodes:
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

graph = {
              's': {('a', 1), ('c', 4)},
              'a': {('b', 2)}, # 'a': {'b'},
              'b': {('c', 1), ('d', 4)}, 
              'c': {('d', 3)},
              'd': {},
              'e': {('d', 0)}
          }
bfs_path(graph, 's')



    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    
    def gp_recursive(result, destination):
        
        if destination == None:
            return result
        
        else:
            is_traceable = False
            for parent in parents:
                if parent == parents[destination]:
                    destination = parent
                    result = result + parents[destination]
                    is_traceable = True
            if is_traceable:
                destination = None
            return gp_recursive(result, destination)
        
    result = parents[destination]
    return gp_recursive(result, destination)




