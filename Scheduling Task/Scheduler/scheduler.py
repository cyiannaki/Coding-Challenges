import pandas as pd
import Routes.routes

class Scheduler(object):
    def __init__(self, routes, *args):
        if not isinstance(args[0], Routes.routes.Routes):
            raise TypeError("Wrong class parameters")
        
        self.routes = routes
        self.resources = {}
        
        for _ in range(0, len(args)):
            self.resources[_] = args[_]              
    
    def best_route(self):   
        all_routes = self.resources[0].route_distances(self.routes, self.resources)
        all_routes_df = pd.DataFrame(all_routes, columns=['Routes', 'Distances'])
        all_routes_df = all_routes_df[all_routes_df['Distances'] == min(all_routes_df['Distances'])]
        return all_routes_df
        
        
