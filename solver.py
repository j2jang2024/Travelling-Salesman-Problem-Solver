from math import sqrt
import random

def readTSP(filename):
    # "burma14.tsp"
    f = open(filename,"r")
    myList = []
    start = False
    for line in f:
        lineSplitted = line.split()
        if "NODE_COORD_SECTION" in lineSplitted:
            start = True
            continue
        if start:
            if "EOF" in lineSplitted:
                break
            myList.append((float(lineSplitted[1]),float(lineSplitted[2])))

    return myList

def pythagoras(p1, p2):
    d = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d

def getTotalDistance(order):
    dis = 0
    for i in range(len(order)-1):
        dis += pythagoras(order[i], order[i+1])
    dis += pythagoras(order[-1], order[0])
    return dis

def greedySeed(points):
    templen = len(points)
    distance = 0
    order = []
    first_point = points.pop(random.choice(range(len(points))))
    
    for x in range(templen-1):
        current = points[0]
        for point in points:
            if pythagoras(first_point, point) < pythagoras(first_point, current):
                current = point
        order.append(current)
        distance += pythagoras(first_point, current)
        first_point = current
        points.remove(current)
    return order
    
def randomSeed(points):
    random.shuffle(points)
    return points

def twoPointSwap(order):
    old_dist = getTotalDistance(order)
    a = random.choice(range(len(order)))
    b = random.choice(range(-5, 5))
    while b == 0:
        b = random.choice(range(-5, 5))
    b += a
    if b >= len(order):
        b -= len(order)
    a_temp = order[a]
    order[a] = order[b]
    order[b] = a_temp

    return order

init = readTSP('rl11849.tsp')
temp = greedySeed(init)
org_dist = getTotalDistance(temp)
print("Initial Distance: " + str(org_dist))

for i in range(10000):
    new_order = twoPointSwap(temp)
    new_dist = getTotalDistance(new_order)
    if new_dist<org_dist:
        print("Success! " + str(new_dist))
        temp = new_order
        org_dist=new_dist
    
    

#print(greedySeed(readTSP("burma14.tsp")))
#print(randomSeed(readTSP("burma14.tsp")))