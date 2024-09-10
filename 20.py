import modules
import sys

sys.setrecursionlimit(10000)

input = open(r"C:\Users\Jens\Desktop\AoC\2023\20\input.txt")
lines = input.readlines()
data = []
for line in lines:
    newline = line.strip('\n')
    data.append((newline))

def splitLine(line):
    idx_arrow = line.find(">")
    destinations = line[idx_arrow+2:]
    listofdestinations = destinations.split(', ')
    name = line[1:idx_arrow-2]
    module_type = line[0]
    return module_type, name, listofdestinations

def getInputdict(data):
    name_dest = {}
    conj_input = {}
    conj_modules = []
    for line in data:
        idx_arrow = line.find(">")
        destinations = line[idx_arrow+2:]
        listofdestinations = destinations.split(', ')
        name = line[1:idx_arrow-2]
        module_type = line[0]    
        name_dest[name] = listofdestinations
        if module_type == "&":
            conj_modules.append(name)

    for conj_module in conj_modules:
        list = []
        for mod,dlist in name_dest.items():
            if conj_module in dlist:
                list.append(mod)
        conj_input[conj_module] = list

    return conj_input

inputdict = getInputdict(data)
listofmodules = []


for line in data:
    module_type, name, listofdestinations = splitLine(line)
    if module_type == "&":
        inputlist = inputdict[name]
        entry = modules.Conjunction(inputlist, listofdestinations, name)
        listofmodules.append(entry)
    elif module_type == "%":
        entry = modules.Flipflop(listofdestinations,name)
        listofmodules.append(entry)
    else:
        entry = modules.Broadcast(listofdestinations)
        listofmodules.append(entry)

def splitListOfModules(listofmodules):
    listofflipflops = []
    listofconjunctions = []
    for module in listofmodules:
        if isinstance(module,modules.Conjunction):
            listofconjunctions.append(module)
        elif isinstance(module,modules.Flipflop):
            listofflipflops.append(module)
    return listofconjunctions, listofflipflops

def cycle(listofmodules, low, high):
    pulse = '-'
    firstmodule = listofmodules[0]
    sender = 'Button'
    listofpulses = [(firstmodule.name,pulse,sender)]

    while listofpulses:
        sender = listofpulses[0][2]
        module = modules.getModulebyName(listofpulses[0][0], listofmodules)
        pulse = listofpulses[0][1]
        if pulse == '-':
            low += 1
        else:
            high += 1
        # am anfang ein conj module?
        if isinstance(module,modules.Conjunction):
            module.updateMemory(sender,pulse)
        newpulse = module.process(pulse)
        destinations = module.destinations
        for destination in destinations:
            if newpulse != None:
                if destination == 'rx':
                    if newpulse == '-':
                        low += 1
                    else:
                        high += 1
                else:
                    listofpulses.append((destination, newpulse, module.name))
        listofpulses.pop(0)

    return(listofmodules, low, high)

def multiplecycles(listofmodules, ctr, low, high):
    listofmodules, low, high = cycle(listofmodules,low,high)
    if ctr == 1000:
        return low,high
    else:
        return multiplecycles(listofmodules, ctr+1, low,high)
    
print(multiplecycles(listofmodules,1,0,0))
