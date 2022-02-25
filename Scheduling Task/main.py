import pandas as pd
from collections import namedtuple
from itertools import combinations, permutations

class Graph(object):
    def __init__(self):
        #Edges are placed in this class and not in main() because lists are mutable and any changes in the obj are reflected in the passed argument
        self.edges =  {   "A1": [0, 13, 25, 10, 32, 24, 10, 45, 13, 8],
                          "A2": [13, 0, 14, 16, 19, 13, 7,	32,	13,	18],
                          "A3": [25, 14, 0, 24, 10, 19, 21, 25, 17, 32],
                          "A4": [10, 16, 24, 0, 32,	29,	17,	47,	7, 18],
                          "A5": [32, 19, 10, 32, 0, 16, 25, 15, 26, 37],
                          "A6": [24, 13, 19, 29, 16, 0, 14, 23, 26, 26],
                          "A7": [10, 7, 21, 17, 25, 14, 0, 37, 18, 12],
                          "A8": [45, 32, 25, 47, 15, 23, 37, 0, 42, 49],
                          "A9": [13, 13, 17, 7, 26, 26, 18, 42, 0, 22],
                         "A10": [8, 18, 32, 18, 37, 26, 12, 49, 22, 0]}
        self.graph = ""
        self.routes = ""
        self.translation = {"A1": 0, "A2": 1, "A3": 2, "A4": 3, "A5": 4,
                            "A6": 5, "A7": 6, "A8": 7, "A9": 8, "A10": 9}
        self.max_activities = 0

    def update_edges(self, route):
        #Updates the matrix diagonally with the home to work distances
        position = 0
               
        for index, edge in self.edges.items():
            edge[position] = route[position]
            position += 1
            
class Routes(Graph):
    def route_permutations(self):
        #Combination of routes
        self.routes = list(permutations(self.graph.nodes, self.max_activities))      
        print("Total route permutations:{}".format(len(self.routes)))
    
    def route_distances(self):
        all_distances = []
        
        for route in self.routes: #First loop gets a selection of unique activities
            translated_route = []
            [translated_route.append(self.translation[activity]) for activity in route] #Translate route to an index position
             
            #To get the edges, i need to specify x and y index positions for the matrix 
            start = translated_route[0]
            distance = 0
        
            for indx in translated_route:
               distance += list(self.edges.values())[start][indx]
               start = indx
               
            #Add distance from final location to home
            distance += self.graph.resource[start]
            all_distances.append([route, distance])
        
        return all_distances
    
class Scheduler(object):
    def __init__(self, *args):
        self.r1_obj = args[0]
        self.r2_obj = args[1]
    
    def best_route(self):
        r1_routes = self.r1_obj.route_distances()
        r2_routes = self.r2_obj.route_distances()
        total_activities = self.r1_obj.max_activities + self.r2_obj.max_activities
        all_results = []
        count = 0
        min_dist = 9999
        
        for r1 in r1_routes:  
            temp_results = []
            
            for r2 in r2_routes:
                result = r1[0] + r2[0] #join R1 activities to R2 activities
                distance = r1[1] + r2[1] # total distance for both activities
                
                if distance < min_dist: #ignore distances greater than the minimum distance           
                    number_of_act = len(list(set(result))) #set removes duplicates since there should be no overlap of activities
                
                    if number_of_act == total_activities: #filter out activities that have less than 10 activities
                       min_dist = distance            
                       temp_results.append([result, distance, number_of_act])
            
            if len(temp_results) > 0:
                all_results.append(temp_results[-1])
                print(temp_results[-1])
        
        return all_results
        
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
    r1_obj = Routes()
    r1_obj.update_edges(r1)
    r2_obj = Routes()
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
    sched_obj = Scheduler(r1_obj, r2_obj)
    best_routes = sched_obj.best_route()
    best_routes = pd.DataFrame(best_routes, columns=['Route', 'Distance', 'Total Activities'])
    print("Best route parameters:")
    print("R1: {}, R2: {} \n".format(r1_obj.max_activities, r2_obj.max_activities))
    print("Best result:")
    print(best_routes.iloc[-1])