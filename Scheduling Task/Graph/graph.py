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
        if type(route) is not list:
            raise TypeError("Invalid 'route' param data type not iterable")
        
        if any([True for r in route if type(r) != int]):       
            raise ValueError("Route value not an int")
            
        position = 0
               
        for index, edge in self.edges.items():
            edge[position] = route[position]
            position += 1
            