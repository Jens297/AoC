class Node:
    def __init__(self,x,y,dx,dy,steps):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.steps = steps
        self.cost = float('inf')


    def __str__(self):
        return f"({self.x}, {self.y}, {self.dx}, {self.dy}, {self.steps}, {self.cost})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.x == other.x and
                    self.y == other.y and
                    self.dx == other.dx and
                    self.dy == other.dy and
                    self.steps == other.steps)
        return False
    def __hash__(self):
        return hash((self.x, self.y, self.dx, self.dy, self.steps))
