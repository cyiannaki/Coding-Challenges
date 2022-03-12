import pandas as pd
from collections import namedtuple
import Routes.routes as routes
import Scheduler.scheduler as scheduler
        
if __name__ == "__main__":
    """
    Vertex / Node: 1 to 10
    Edge: The distance between 2 nodes
    """    
    graph = namedtuple("Graph", ["nodes", "edges", "resource"]) #tuples are immutable
    nodes = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
    
        # A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
    r1 = [15,15,18, 7,28,28,20,43, 2,24]
    r2 = [6, 11,25,16,30,19, 5,42,18, 7]
   
    #Build the routes for the resource 1 and 2   
    r1_obj = routes.Routes()
    r1_obj.update_edges(r1)
    r2_obj = routes.Routes()
    r2_obj.update_edges(r2)
    
    #Update the tuples to contain all the data in a named tuples
    r1_obj.graph = graph(nodes, r1_obj.edges, r1)
    r2_obj.graph = graph(nodes, r2_obj.edges, r2)
 
    #Get combination of all available routes
    r1_obj.max_activities = 4 #can be changed to 5 and 5 or 6 and 4     
    r2_obj.max_activities = 6
    r1_obj.route_permutations()
    r2_obj.route_permutations()
    
    #Create schedule with shortest route
    sched_obj = scheduler.Scheduler(r1_obj, r2_obj)
    best_routes = sched_obj.best_route()
    best_routes = pd.DataFrame(best_routes, columns=['Route', 'Distance', 'Total Activities'])
    print("Best route parameters:")
    print("R1: {}, R2: {} \n".format(r1_obj.max_activities, r2_obj.max_activities))
    print("Best result:")
    print("R1: ", best_routes.iloc[-1].Route[:r1_obj.max_activities])
    print("R2: ", best_routes.iloc[-1].Route[r1_obj.max_activities:])
