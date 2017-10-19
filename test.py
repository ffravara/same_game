import copy
lista = [[(0, 0)], [(0, 1), (1, 1), (0, 2), (1, 2)], [(0, 3), (0, 4), (1, 4)], [(2, 4), (2, 3), (2, 2)]]
lista2=[[(0, 0)], [(0, 1), (1, 1), (0, 2), (1, 2)], [(0, 3), (0, 4), (1, 4)], [(2, 4), (2, 3), (2, 2), (2, 1)]]



def inGroup(groupBoard, pos):
    return groupBoard[pos_l(pos)][pos_c(pos)]
def nowInGroup(groupBoard,pos):
    groupBoard[pos_l(pos)][pos_c(pos)]=True

def appendGroups(groups,pos1,pos2):
    i=GetGroupIndex(groups,pos1)
    j=GetGroupIndex(groups,pos2)
    print(i)
    print(j)
    new_list=copy.deepcopy(groups[i])

    if (i!=j):
        for el in groups[j]:
            new_list.append(el)
        del groups[i]
        del groups[j-1]
        groups.append(new_list)


def GetGroupIndex(groups,pos):
    index = -1
    for sublist in groups:
        index=index + 1
        if pos in sublist:
            return index


appendGroups(lista2, (0,1),(2,2))
print (lista2)

"""
def printBoard(t):
    i=0
    j=0
    for i in range(lines(t)):
        print( getLine(t,i))

print(visited)"""
