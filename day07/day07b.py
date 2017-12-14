import sys

"""get the weight of the given node and its subtowers"""
def getWeight(tower, subTowers, weights):
    weight = weights[tower] #include ourselve
    for subTower in subTowers[tower]:
        weight += getWeight(subTower, subTowers, weights)
    #print("tower: ", tower, " has self weight=", weights[tower], "final=", weight)
    return weight

"""find the most common weight in set of 3+"""
def correctWeight(children, subTowers, weights):
    clone = children.copy()
    avg = [getWeight(clone.pop(), subTowers, weights) for i in range(3)]
    if avg[0] == avg[1]:
        return avg[0]
    if avg[1] == avg[2]:
        return avg[1]
    return avg[2]

def bfs(node, subTowers, weights):
    if len(subTowers[node]) == 0:
        print("fault at", node)
        return -1
    children = subTowers[node]
    wanted = correctWeight(children, subTowers, weights)
    problem = ""
    for i in children:
        if getWeight(i, subTowers, weights) != wanted:
            problem = i
            break
    if problem == "":
        return -1
    if bfs(i, subTowers, weights) == -1:
        print(i, "has weight", weights[i], "expected", wanted - len(subTowers[i]) * correctWeight(subTowers[i], subTowers, weights))
        return wanted


file = open(sys.argv[1])
bottom = ""
weights = dict()
subTowers = dict()
above = set()
for line in file:
    parts = line.split()
    weights[parts[0]] = int(parts[1][1:-1])
    subTowers[parts[0]] = set()
    for i in parts[3:]:
        program = ""
        if (i.endswith(",")):
            program = i[0:-1]
        else:
            program = i
        above.add(program)
        subTowers[parts[0]].add(program)
file.close()

root = set(weights.keys()).difference(above).pop()

bfs(root, subTowers, weights)

