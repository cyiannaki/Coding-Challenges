import pandas as pd
from collections import namedtuple
import Routes.routes as routes
import Scheduler.scheduler as scheduler
import time
        
if __name__ == "__main__":
    """
    Vertex / Node: 1 to 10
    Edge: The distance between 2 nodes
    """
    timer_start = time.process_time()    
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
    total_activities = r1_obj.max_activities + r2_obj.max_activities
    routes = r1_obj.route_permutations(total_activities)

    #Create schedule with shortest route
    sched_obj = scheduler.Scheduler(routes, r1_obj, r2_obj)
    timer_start = time.process_time()
    best_routes = sched_obj.best_route()
    best_routes = pd.DataFrame(best_routes, columns=['Routes', 'Distances'])
    
    print("Best route parameters:")
    print("R1: {}, R2: {} \n".format(r1_obj.max_activities, r2_obj.max_activities))
    print("Best results:")   
    best_routes['R1 Routes'] = best_routes['Routes'].apply(lambda x: x[:r1_obj.max_activities])
    best_routes['R2 Routes'] = best_routes['Routes'].apply(lambda x: x[r1_obj.max_activities:])
    print(best_routes[['R1 Routes', 'R2 Routes', 'Distances']])
    
    timer_end = time.process_time()
    res = timer_end - timer_start
    print('CPU Execution time:', res, 'seconds')
    
    """
    runfile('/home/charlie/Desktop/Scheduling Task/main.py')
    Reloaded modules: Graph.graph, Routes.routes, Scheduler.scheduler
    
    Total route permutations:3628800
    Route Distance Calculations
    100%|██████████| 3628800/3628800 [00:24<00:00, 146981.38it/s]
    
    Best route parameters:
    R1: 4, R2: 6 
    
    Best results:
                     R1 Routes                 R2 Routes  Distances
    1415524  (A4, A10, A1, A9)  (A2, A3, A5, A8, A6, A7)        140
    1416095  (A4, A10, A1, A9)  (A7, A6, A8, A5, A3, A2)        140
    2939764  (A9, A1, A10, A4)  (A2, A3, A5, A8, A6, A7)        140
    2940335  (A9, A1, A10, A4)  (A7, A6, A8, A5, A3, A2)        140
    
    CPU Execution time: 26.340114893999996 seconds
    
    Analysis: Only 1 valid route since A4 cannot be visited by another route.
              All the activities are the same.    
    """
