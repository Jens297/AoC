from node import Node
from copy import deepcopy


# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\19\input.txt")
# read it line by line
lines = input.readlines()
data = []
for line in lines:
    newline = line.strip('\n')
    data.append((newline))
#print(data)

separator = data.index('')

workflows = data[:separator]
parts = data[separator+1:]

def splitRule(rule):
    doublepontidx = rule.find(':')
    if doublepontidx == -1:
        destination = rule
        condition = ""
    else:
        category = rule[0]
        operator = rule[1]
        comparevalue = rule[2:doublepontidx]
        destination = rule[doublepontidx+1:]
        condition = category+operator+comparevalue
    return (destination,condition)

def splitWorkflowstoRules(workflow):
    listofrules = []
    leftBracket = workflow.index('{')
    rightBracket = workflow.index('}')
    destination = workflow[:leftBracket]
    rules = workflow[leftBracket+1:rightBracket]
    splittedRules = rules.split(',')
    for rule in splittedRules:
        r = splitRule(rule)
        listofrules.append(r)
    return destination, listofrules

def createWorkflowDict(workflows):
    mydict = {}
    x = 0
    for workflow in workflows:
        split = splitWorkflowstoRules(workflow)
        new_list = []
        for element in split[1]:
            # if destination is A: create a single destination of Ax 
            if element[0] == 'A':
                new_tuple = ('A'+ str(x), element[1])
                x += 1
                new_list.append(new_tuple)
            else:
                new_list.append(element)
        mydict.update({split[0]:new_list})
    return mydict, x

# update the dict with every single Ax destination
mydict, x = createWorkflowDict(workflows)
for x in range(x):
    mydict.update({'A'+str(x):[]})
mydict.update({'R':[]})

#print(mydict)

def create_list_of_nodes(dict):
    nodes = []
    for entry in dict:
        node = Node(entry,dict[entry],[])
        nodes.append(node)
    return nodes

nodes = create_list_of_nodes(mydict)

def getNode(nodes,name):
    for node in nodes:
        if node.name == name:
            return node

# invert a condition 
def invertCondition(condition):
    if condition == "":  
        return ""
    else:
        variable = condition[0]
        operator = condition[1]
        compareValue = condition[2:]

        if operator == "<":
            new_operator = ">"
            new_compareValue = str(int(compareValue)-1)
        else:
            new_operator = "<" 
            new_compareValue = str(int(compareValue)+1)           
        return variable+new_operator+new_compareValue
        
# invert all conditions of a node
def updateConditions(node):
    dests = node.destinations
    for idx in range(len(dests)-1):
        conditions = dests[idx][1]
        lastcondition = conditions[0]
        invertedCondition = invertCondition(lastcondition)        
        node.destinations[idx+1][1] = node.destinations[idx+1][1]+conditions[1:]+[invertedCondition]
    return node

for node in nodes:
    node = updateConditions(node)

# get all ways to the accedpted destinations
def findways(nodes, startnode):
    all_paths = []
    to_explore = [startnode]

    while to_explore:
        current_node = to_explore.pop(0)
        new_nodes = []
        current_path = current_node.path_to_reach
        if 'A' in current_node.name:
            all_paths.append(current_node.path_to_reach)
        for d in current_node.destinations:
            new_node = getNode(nodes,d[0])
            new_node.path_to_reach = deepcopy(current_path)
            new_node.path_to_reach.append((d[0],d[1]))
            new_nodes.append(new_node)
        to_explore = new_nodes + to_explore

    return all_paths 
        
start = getNode(nodes,'in')
start.path_to_reach = [('in','')]
paths = findways(nodes, start)

# gets a path and returns the result of its combinations
def getCombinations(path):
    variables = ['a','m','s','x']
    mydict = {}
    for v in variables:
        mydict.update({v:(1,4000)})
    for element in path:
        conditions = element[1]
        for condition in conditions:
            if condition != '':
                variable = condition[0]
                operator = condition[1]
                comparevalue = int(condition[2:])
                ceilings = mydict[variable]
                if operator == '<':
                    ceilings = (ceilings[0],comparevalue-1)
                    mydict[variable] = ceilings
                else:
                    ceilings = (comparevalue+1,ceilings[1])
                    mydict[variable] = ceilings
    result = 1
    for entry in mydict:
        ceilings = mydict[entry]
        result *= (ceilings[1] - ceilings[0]+1)
    return result


def PartB(paths):
    result = 0
    for path in paths:
        result += getCombinations(path)
    return result

print(PartB(paths))
