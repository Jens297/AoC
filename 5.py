# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\5\input.txt")
# read it line by line
lines = input.readlines()
data = []
for line in lines:
    newline = line.strip('\n')
    data.append((newline))

datawithoutspaces = []
for line in data:
    if (line != ""):
        datawithoutspaces.append(line)

SEEDTOSOILIDX = datawithoutspaces.index('seed-to-soil map:')
SOILTOFERTILIZERIDX = datawithoutspaces.index('soil-to-fertilizer map:')
FERTILIZERTOWATERIDX = datawithoutspaces.index('fertilizer-to-water map:')
WATERTOLIGHTIDX = datawithoutspaces.index('water-to-light map:')
LIGHTTOTEMPERATUREIDX = datawithoutspaces.index('light-to-temperature map:')
TEMPERATURETOHUMIDITYIDX = datawithoutspaces.index('temperature-to-humidity map:')
HUMIDITYTOLOCATIONIDX = datawithoutspaces.index('humidity-to-location map:')

#print(datawithoutspaces)

x = datawithoutspaces[0]
y = x.split(' ')
SEEDSASSTRINGS = y[1:]
SEEDS = []
for seed in SEEDSASSTRINGS:
    s = int(seed)
    SEEDS.append(s)
#print('SEEDS', SEEDS)

test = ['50 98 2', '52 50 48']

def convertStringtoListofInts(listofstrings):
    listofints = []
    listoflists = []
    for element in listofstrings:
        x = element.split(' ')
        listofints.append(x)
    for e in listofints:
        l = []
        for v in e:
            v = int(v)
            l.append(v)
        listoflists.append(l)

    return listoflists

def getValues(data, nameofvalue):
    if nameofvalue == 'SEEDTOSOIL':
        SEEDTOSOILVALUES = convertStringtoListofInts(data[SEEDTOSOILIDX+1:SOILTOFERTILIZERIDX])
        return SEEDTOSOILVALUES
    if nameofvalue == 'SOILTOFERTILIZER':
        SOILTOFERTILIZERVALUES = convertStringtoListofInts(data[SOILTOFERTILIZERIDX+1:FERTILIZERTOWATERIDX])
        return SOILTOFERTILIZERVALUES
    if nameofvalue == 'FERTILIZERTOWATER':
        FERTILIZERTOWATERVALUES = convertStringtoListofInts(data[FERTILIZERTOWATERIDX+1:WATERTOLIGHTIDX])
        return FERTILIZERTOWATERVALUES
    if nameofvalue == 'WATERTOLIGHT':
        WATERTOLIGHTVALUES = convertStringtoListofInts(data[WATERTOLIGHTIDX+1:LIGHTTOTEMPERATUREIDX])
        return WATERTOLIGHTVALUES
    if nameofvalue == 'LIGHTTOTEMPERATURE':
        LIGHTTOTEMPERATUREVALUES = convertStringtoListofInts(data[LIGHTTOTEMPERATUREIDX+1:TEMPERATURETOHUMIDITYIDX])
        return LIGHTTOTEMPERATUREVALUES
    if nameofvalue == 'TEMPERATURETOHUMIDITY':
        TEMPERATURETOHUMIDITYVALUES = convertStringtoListofInts(data[TEMPERATURETOHUMIDITYIDX+1:HUMIDITYTOLOCATIONIDX])
        return TEMPERATURETOHUMIDITYVALUES
    if nameofvalue == 'HUMIDITYTOLOCATION':
        HUMIDITYTOLOCATIONVALUES = convertStringtoListofInts(data[HUMIDITYTOLOCATIONIDX+1:])
        return HUMIDITYTOLOCATIONVALUES
    
#print('LOCATIONVALUES', getValues(datawithoutspaces, 'HUMIDITYTOLOCATION'))


testsoils = [[60, 56, 37], [56, 93, 4]]

# seed is an int, soils is a list of lists of ints: [[50, 98, 2], [x,y,z]]
def getSoilforSeed(seed, soils):
    numberOfSoils = len(soils)
    for x in range(numberOfSoils):
        DESTRANGESTART = int(soils[x][0])
        SOURCERANGESTART = int(soils[x][1])
        RANGELENGTH = int(soils[x][2])
        SOURCERANGEEND = SOURCERANGESTART+RANGELENGTH
        if SOURCERANGESTART <= seed <= SOURCERANGEEND:
            #print("Source", seed, 'is in range', SOURCERANGESTART, 'to', SOURCERANGESTART+RANGELENGTH)
            DIFF = seed-SOURCERANGESTART
            #print('DIFF',DIFF, 'DESTSTAR', DESTRANGESTART)
            result = DESTRANGESTART+DIFF
            return(result)
        else:
            result = seed
    return(result)

#print('Seeds:', SEEDS)

def seedsToLocation(seed, data):
    #(print('Seed', seed))
    seed = getSoilforSeed(seed, getValues(data, 'SEEDTOSOIL'))
    #(print('Soil', seed))
    seed = getSoilforSeed(seed, getValues(data, 'SOILTOFERTILIZER'))
    #(print('Fertilizer', seed))
    seed = getSoilforSeed(seed, getValues(data, 'FERTILIZERTOWATER'))
    #(print('Water', seed))
    seed = getSoilforSeed(seed, getValues(data, 'WATERTOLIGHT'))
    #(print('Light', seed))
    seed = getSoilforSeed(seed, getValues(data, 'LIGHTTOTEMPERATURE'))
    #(print('Temperature', seed))
    seed = getSoilforSeed(seed, getValues(data, 'TEMPERATURETOHUMIDITY'))
    #(print('Humidity', seed))
    seed = getSoilforSeed(seed, getValues(data, 'HUMIDITYTOLOCATION'))
    #(print('Location', seed))
    return seed
    
#print(seedsToLocation(SEEDS, datawithoutspaces))

testseedlist = [79, 14, 55, 13]

def solveB(data, seedstart, seedrange):
    result = 10000000000
    seedend = seedstart+seedrange
    seeds = range(seedstart,seedend)
    for seed in seeds:
        #currentseed = next(seedgenerator)
        print('current seed',seed)
        currentlocation = seedsToLocation(seed,data)
        #print('Current Location:', currentlocation)
        result = currentlocation
        if currentlocation < result:
            result = currentlocation
            print(result)
    return result

#print(solveB(datawithoutspaces,1132132257, 323430997)) #1455563254

# 2043754183 4501055 
# 2539071613 1059028389 
# 1695770806 60470169 
# 2220296232 251415938 
# 1673679740 6063698 
# 962820135 133182317 
# 262615889 327780505 
# 3602765034 194858721 
# 2147281339 37466509


# Definierte Ranges
sourceranges = [range(0,10), range(11,20), range(25,30)]
seedrange = range(0,35)

# Hilfsfunktion, um zu überprüfen, ob ein Wert in einem der sourceranges liegt
def is_in_sourceranges(value, sourceranges):
    return any(value in r for r in sourceranges)

# Hilfsfunktion, um aus einer Liste von Werten Ranges zu erstellen
def ranges_from_list(values):
    if not values:
        return []
    
    ranges = []
    start = values[0]
    current = values[0]

    for value in values[1:]:
        if value == current + 1:
            current = value
        else:
            ranges.append(range(start, current + 1))
            start = value
            current = value

    ranges.append(range(start, current + 1))
    return ranges

def split_ranges(seedrange, sourceranges):

    # Listen für die Werte in und außerhalb der sourceranges
    matching_values = []
    non_matching_values = []

    # seedrange aufteilen
    for value in seedrange:
        if is_in_sourceranges(value, sourceranges):
            matching_values.append(value)
        else:
            non_matching_values.append(value)

    # Erstellen der Ranges aus den Werten
    matching_ranges = ranges_from_list(matching_values)
    non_matching_ranges = ranges_from_list(non_matching_values)

    return matching_ranges, non_matching_ranges

# Beispielaufruf
sourceranges = [range(0,10), range(11,20), range(25,30)]
seedrange = range(0,35)

matching_ranges, non_matching_ranges = split_ranges(seedrange, sourceranges)

# Ergebnis
print("Matching ranges:", matching_ranges)
print("Non-matching ranges:", non_matching_ranges)
