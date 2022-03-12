import pytest, random
import Routes.routes as routes
import pandas as pd
from collections import namedtuple

"""
Functionality testing of routes class
"""
def initialize():
    graph = namedtuple("Graph", ["nodes", "edges", "resource"]) #tuples are immutable
    nodes = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
    route_obj = routes.Routes()
    r1 = [15,15,18, 7,28,28,20,43, 2,24]
    route_obj.update_edges(r1)
    route_obj.graph = graph(nodes, route_obj.edges, r1)
    route_obj.max_activities = 5
    route_obj.route_permutations()
    return route_obj

def test_match_single_permutation():
    #Chech if a random choice of 5 activities exists in all the permutations
    route_obj = initialize()
    test_route = tuple([random.choice(route_obj.graph.nodes) for x in range(0, 5)])
    assert test_route in route_obj.routes

def test_single_route_distance():
    #Verify that the distance of a route is correct
    route_obj = initialize()
    r1_routes = route_obj.route_distances()
    test_route = ('A4', 'A1', 'A7', 'A5', 'A10')
    test_route_dist = 7+10+10+25+37+24  
    
    r1_routes_df = pd.DataFrame(r1_routes)
    r1_routes_df.columns = ['Activity', 'Distance']
    actual_distance = r1_routes_df.Distance[r1_routes_df.Activity == test_route].iloc[0]
    assert actual_distance == test_route_dist
