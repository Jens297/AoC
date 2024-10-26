class node:
    def __init__(self,coords,cost):
        self.g = None
        self.f = None
        self.h = None
        self.cost = cost
        self.coords = coords
        self.last_direction = None 
        self.steps_in_direction = 0 


    def __str__(self):
        return str(self.coords,self.f,self.g,self.h)
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.coords == other.coords
    def __hash__(self):
        return hash((self.coords))
