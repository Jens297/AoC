class Brick:
    def __init__(self,tag,x,y,z,xx,yy,zz):
        self.x = x
        self.y = y
        self.z = z
        self.xx = xx
        self.yy = yy
        self.zz = zz
        self.tag = tag
        self.supports = []
        if z == zz:
            self.horicontal = True
        else:
            self.horicontal = False


    def __str__(self):
        return f"({self.tag}, {self.x}, {self.y}, {self.z}, {self.xx}, {self.yy}, {self.zz}, {self.supports}, {self.horicontal})"
    def __repr__(self):
        return self.__str__()
