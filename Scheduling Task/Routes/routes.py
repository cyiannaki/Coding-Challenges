import Graph.graph as graph
from itertools import permutations

class Routes(graph.Graph):    
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
