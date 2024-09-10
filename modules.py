class Flipflop:
    def __init__(self,destinations,name):
        self.state = 'off'
        self.name = name
        self.destinations = destinations
    
    def display_message(self):
        print(self.state)
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

    def process(self,pulse):
        if pulse == '-':
            if self.state == 'off':
                self.state = 'on'
                return '+'
            else:
                self.state = 'off'
                return '-'
            
class Broadcast:
    def __init__(self,destinations):
        self.name = "Broadcast"
        self.destinations = destinations
        
    def process(self,pulse):
        if pulse == '-':
            return '-'
        else:
            return '+'
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
        

class Conjunction:
    def __init__(self, inputlist, destinations, name):
        self.memory = {value: '-' for value in inputlist}
        self.name = name
        self.destinations = destinations

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()
    
    def process(self,pulse):
        if all(value == '+' for value in self.memory.values()):
            return "-"
        else:
            return "+"
    
    def updateMemory(self,sender,pulse):
        self.memory[sender] = pulse
        
def getModulebyName(name, listofmodules):
    for module in listofmodules:
        if module.name == name:
            return module
    else:
        return "no module with name", name, "in the list"

# returns true if every ff is off 
def checkFlipflopStates(listofflipflops):
    for ff in listofflipflops:
        if ff.state == 'on':
            return False
    return True

#returns true if every memory is on initial state
def checkConjMemory(listofconjunctions):
    for c in listofconjunctions:
        if all(value == '-' for value in c.memory.values()):
            return True
    return False
