import random
import Routes.routes as routes
import pandas as pd
from collections import namedtuple

"""
Functionality testing of routes class
"""
def initialize():
    graph = namedtuple("Graph", ["nodes", "edges", "resource"]) #tuples are immutable
    nodes = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
    route_obj1 = routes.Routes()
    route_obj2 = routes.Routes()
    
    r1 = [15,15,18, 7,28,28,20,43, 2,24]
    r2 = [6, 11,25,16,30,19, 5,42,18, 7]
    
    route_obj1.update_edges(r1)
    route_obj1.graph = graph(nodes, route_obj1.edges, r1)
    route_obj1.max_activities = 4
    route_obj2.update_edges(r2)
    route_obj2.graph = graph(nodes, route_obj2.edges, r2)
    route_obj2.max_activities = 6
    
    route_perm = route_obj1.route_permutations(10)
    
    return route_obj1, route_obj2, route_perm

def test_match_single_permutation():
    #Chech if a random choice of 5 activities exists in all the permutations
    route_obj, route_obj2, route_perm = initialize()
    test_route = []
    
    while len(test_route) < 10:    
        test_route.append(random.choice(route_obj.graph.nodes))
        test_route = list(set(test_route))
    
    assert tuple(test_route) in route_perm

def test_single_route_distance():
    #Verify that the distance of a route is correct
    route_obj1, route_obj2, route_perm = initialize()
    route_obj_dict = {0:route_obj1, 1:route_obj2}
    
    r1_routes = route_obj1.route_distances(route_perm, route_obj_dict)
    test_route = ('A4', 'A10', 'A1', 'A9', 'A2', 'A3', 'A5', 'A8', 'A6', 'A7') 
    test_route_dist = 140
    
    r1_routes_df = pd.DataFrame(r1_routes)
    r1_routes_df.columns = ['Activity', 'Distance']
    actual_distance = r1_routes_df.Distance[r1_routes_df.Activity == test_route].iloc[0]
    assert actual_distance == test_route_dist
    
if __name__ == '__main__':
    test_single_route_distance()