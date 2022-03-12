import pytest
import Scheduler.scheduler as scheduler

"""
Test wrong scheduler parameters
"""
def test_scheduler_incorrect_number_of_resources():
    #For this task there are only 2 resource objects but 3 will be given
    with pytest.raises(IndexError, match="Incorrect number of resources"):
        scheduler.Scheduler(object, object, object)

"""
Functionality testing of scheduler class
"""
# def initialize():
#     graph = namedtuple("Graph", ["nodes", "edges", "resource"]) #tuples are immutable
#     nodes = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
#     route_obj = routes.Routes()
#     r1 = [15,15,18, 7,28,28,20,43, 2,24]
#     route_obj.update_edges(r1)
#     route_obj.graph = graph(nodes, route_obj.edges, r1)
#     route_obj.max_activities = 5
#     route_obj.route_permutations()
#     return route_obj

# def test_best_route_correct_outcome():
#     #Best distance is 140 
#     pass
    