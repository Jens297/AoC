class Node:
    def __init__(self,name,destinations,path_to_reach):
        self.name = name
        self.path_to_reach = []
        self.destinations = destinations

    def __repr__(self):
        if any(self is item for item in self.path_to_reach):
            path_repr = "[...] (self-reference)"
        else:
            path_repr = f"{self.path_to_reach}"
        return (
            f"Node(name={self.name}, "
            f"destinations={[destination for destination in self.destinations]}, "
            f"path_to_reach={path_repr})"
        )
    def __eq__(self, other):
        if isinstance(other, Node):  # check if node
            return self.name == other.name
        return False
