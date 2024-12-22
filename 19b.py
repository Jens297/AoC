from node import Node
from node import Tree
import copy
from copy import deepcopy


# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\19\input.txt")
# read it line by line
lines = input.readlines()
data = []
for line in lines:
    newline = line.strip('\n')
    data.append((newline))

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
    for workflow in workflows:
        split = splitWorkflowstoRules(workflow)
        mydict.update({split[0]:split[1]})
    return mydict

# create a dict to convert it later to a list of nodes
# add A and R as dead ends
mydict = createWorkflowDict(workflows)
mydict.update({'A':[]})
mydict.update({'R':[]})

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

def findways(nodes, startnode):
    all_paths = []
    to_explore = [startnode]

    while to_explore:
        current_node = to_explore[0]
        new_nodes = []
        current_path = current_node.path_to_reach

        for d in current_node.destinations:
            new_node = getNode(nodes,d[0])
            new_node.path_to_reach = deepcopy(current_path)
            new_node.path_to_reach.append((d[0],d[1]))
            new_nodes.append(new_node)
        if current_node.name == "A":
            all_paths.append(current_node.path_to_reach)
        to_explore.pop(0)
        to_explore = new_nodes + to_explore

    return all_paths 

# get start node and set its path to reach to 'in', no condition
start = getNode(nodes,'in')
start.path_to_reach = [('in','')]
paths = findways(nodes, start)

def getCombinations(path):
    variables = ['a','m','s','x']
    mydict = {}
    for v in variables:
        mydict.update({v:(1,4000)})
    for element in path:
        condition = element[1]
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
        result *= (ceilings[1] - ceilings[0])
    return result

def PartB(paths):
    result = 0
    for path in paths:
        result += getCombinations(path)
    return result

print(PartB(paths))
