
t=[[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]

"""TAD board"""

def seeLines(t):
    return len(t)
def seeColumns(t):
    return len(t[0])
def seeLines(t,n):
    return t[n]
def printBoard(t):
    i=0
    j=0
    for i in range(seeLines(t)):
        print( t[i])


"""TAD posicao"""
def make_pos (l, c):
    return (l, c)
def pos_l (pos):
    return pos[0]
def pos_c (pos):
    return pos[1]

def valid_move(t, source, mov):
    lines=seeLines(t)
    columns=seeColumns(t)
    if mov=='u':
        return pos_l(source)>0
    if mov=='d':
        return pos_l(source)<lines-1
    if mov=='l':
        return pos_c(source)>0
    if mov=='r':
        return pos_c(source)<colums-1


def getAdjacents(t,pos):
    adjacents=[]
    if valid_move(t,pos,'u'):
        adjacents.push(make_pos(pos_l(pos)-1, pos_c(pos)))
    if valid_move(t,pos,'l'):
        adjacents.push(make_pos(pos_l(pos), pos_c(pos)-1))
    if valid_move(t,pos,'d'):
        adjacents.push(make_pos(pos_l(pos)+1, pos_c(pos)))
    if valid_move(t,pos,'r'):
        adjacents.push(make_pos(pos_l(pos), pos_c(pos)+1))


    return adjacents



"""TAI color"""
# sem cor = 0
# com cor > 0
def get_no_color():
    return 0
def no_color (c):
    return c==0
def color (c):
    return c > 0
def getColor( t ,pos):
    return t[pos_l(pos)][pos_c(pos)]
def setPositionClor(t,pos,v):
    t[pos_l(pos)][pos_c(pos)]=v



"""TAD group"""

def addToGroup(g,i,pos):
    g[i].append(pos)
def addAnotherGroup(groups,pos):
    groups.append([pos])
def addAnotherGroup(groups, pos1,pos2):
    groups.append([pos1,pos2])



def getGroupOfPos(groups,pos):
    for i in range(len(groups)):
        if pos in groups[i]:
            return i

def inGroup(in_group_board, pos):
    return in_group_board[pos_l(pos)][(new_pos)]

def visited(visited_board,pos):
    return visited_board[pos_l(pos)][pos_c(pos)]
def setVisited(visited_board,pos):
    visited_board[pos_l(pos)][pos_c(pos)]=True






def  board_find_groups(board):

    lines=seeLines(board)
    columns =seeColumns(board)

    visited_board=[[False for i in range(lines)]for j in range(columns)]
    in_group_board=[[False for i in range(lines)]for j in range(columns)]
    stack=[]

    stack.append(make_pos(0,0))
    while stack!=[]:
        pos=stack.pop()
        in_group=False
        for new_pos in getAdjacents(board,pos):
            if visited(visited_board,new_pos):
                if lor(t,new_pos)==getColor(t,pos):
                    addToGroup(groups,getGroupOfPos(groups,new_pos),pos)
                    in_group=True
            else:
                if getColor(t,new_pos)==getColor(t,pos):
                    addAnotherGroup(groups, pos, new_pos)
                    in_group=True
                    stack.push(new_pos)
        if in_group==False:
            addAnotherGroup(groups,pos)
        setVisited(visited_board,pos)
    return groups

print(board_find_groups(t))




"""GREEN TRASH (hopefully not needed recyclabe shit)"""

"""def appendGroups(groups,pos1,pos2):
    i=getGroupOfPos(groups,pos2)
    new_list=groups[i1
    del groups[i]
    j=getGroupOfPos(groups,pos2)
    new_list=new_list+groups[j]
    del groups[j]
    groups.append(new_list)"""



"""def pos_close(pos1,pos2):
    if pos1[0]==pos2[0]:
        if pos1[1]==pos2[1]+1 or pos1[1]==pos2[1]-1:
            return True
    elif pos1[1]==pos2[1]:
        if pos1[0]==pos2[0]+1 or pos1[0]==pos2[0]-1:
            return True
    return False"""

"""def  board_find_groups(board):
    groups=[]
    for i in range(seeLines(board)):
        for j in range(seeColumns(board)):
            iteratingPos= make_pos(i,j)
            iteratingPosAppended=False
            for sublist in groups:
                if iteratingPosAppended==True:
                    break
                for pos in sublist:
                    if iteratingPosAppended==True:
                        break
                    if pos_close(pos,iteratingPos) and getColor(t,pos)==getColor(t,iteratingPos):
                        addToGroup(sublist,iteratingPos)
                        iteratingPosAppended=True
            addAnotherGroup(groups, iteratingPos)
    return groups"""

"""class Same_game(Problem):
    def __init__(self):
        MySuperClass.__init__(self)"""
