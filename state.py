class State:
    def __init__(self,coords,symbol):
        self.coords = coords
        self.symbol = symbol
        self.cameFrom = None
        self.visited  = False
        self.path_to_reach = []
    
    def __eq__(self, other):
        if isinstance(other, State):  # check if node
            return self.coords == other.coords
        return False
    
    def __repr__(self):
        return (
            f"Node(coords={self.coords}, "
            f"symbol={self.symbol}, "
            f"cameFrom={self.cameFrom}, "
            f"visited={self.visited}) "
        )
