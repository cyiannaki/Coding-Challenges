import Graph.graph as graph
from itertools import permutations
from tqdm import tqdm 

class Routes(graph.Graph):    
    def route_permutations(self, max_activities):
        #Combination of routes
        routes = list(permutations(self.graph.nodes, max_activities))      
        print("Total route permutations:{}".format(len(routes)))
        return routes
    
    def route_distances(self, routes, resources):
        all_distances = []
        
        print("Route Distance Calculations")
        
        for route in tqdm(routes): #First loop gets a selection of unique activities
            translated_route = []
            [translated_route.append(self.translation[activity]) for activity in route] #Translate route to an index position
            route_distances = 0 
            
            for resource in resources.values():
                resource_route = translated_route[:resource.max_activities]
                del translated_route[:resource.max_activities]            
                
                #To get the edges, i need to specify x and y index positions for the matrix 
                start = resource_route[0]
                distance = 0
            
                for indx in resource_route:
                   distance += list(resource.edges.values())[start][indx]
                   start = indx
                   
                #Add distance from final location to home
                distance += resource.graph.resource[start]
                route_distances += distance
                           
            all_distances.append([route, route_distances])
        
        return all_distances
