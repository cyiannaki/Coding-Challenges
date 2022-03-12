class Scheduler(object):
    def __init__(self, *args):
        if len(args) != 2:
            raise IndexError("Incorrect number of resources")
        
        self.r1_obj = args[0]
        self.r2_obj = args[1]
    
    def best_route(self):
        r1_routes = self.r1_obj.route_distances()
        r2_routes = self.r2_obj.route_distances()
        total_activities = self.r1_obj.max_activities + self.r2_obj.max_activities
        all_results = []
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