
t=[[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]

"""TAD posicao"""
def make_pos (l, c):
    return (l, c)
def pos_l (pos):
    return pos[0]
def pos_c (pos):
    return pos[1]
def pos_close(pos1,pos2):
    if pos1[0]==pos2[0]:
        if pos1[1]==pos2[1]+1 or pos1[1]==pos2[1]-1:
            return True
    elif pos1[1]==pos2[1]:
        if pos1[0]==pos2[0]+1 or pos1[0]==pos2[0]-1:
            return True
    return False


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

"""TAD board"""

def total_l(t):
    return len(t)
def total_c(t):
    return len(t[0])
def getLine(t,n):
    return t[n]
def printBoard(t):
    i=0
    j=0
    for i in range(total_l(t)):
        print( getLine(t,i))

"""TAD group"""

def addToGroup(g,pos):
    g.append(pos)
def addAnotherGroup(groups,pos):
    groups.append([pos])


def  board_find_groups(board):
    board_groups=[]
    for i in range(total_l(board)):
        for j in range(total_c(board)):
            iteratingPos= make_pos(i,j)
            iteratingPosAppended=False
            for sublist in board_groups:
                if iteratingPosAppended==True:
                    break
                for pos in sublist:
                    if iteratingPosAppended==True:
                        break
                    if pos_close(pos,iteratingPos) and getColor(t,pos)==getColor(t,iteratingPos):
                        addToGroup(sublist,iteratingPos)
                        iteratingPosAppended=True
            addAnotherGroup(board_groups, iteratingPos)
    return board_groups




print(board_find_groups(t))



"""class Same_game(Problem):
    def __init__(self):
        MySuperClass.__init__(self)"""
