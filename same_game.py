
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

def valid_move(t, source, mov):
    lines=lines(t)
    columns=columns(t)
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
    if valid_move(t,pos,'d'):
        adjacents.push(make_pos(pos_l(pos)+1, pos_c(pos)))
    if valid_move(t,pos,'l'):
        adjacents.push(make_pos(pos_l(pos), pos_c(pos)-1))
    if valid_move(t,pos,'u'):
        adjacents.push(make_pos(pos_l(pos)-1, pos_c(pos)))
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

"""TAD board"""

def lines(t):
    return len(t)
def columns(t):
    return len(t[0])
def getLine(t,n):
    return t[n]
def printBoard(t):
    i=0
    j=0
    for i in range(lines(t)):
        print( getLine(t,i))

"""TAD group"""

def addToGroup(g,pos):
    g.append(pos)
def addAnotherGroup(groups,pos):
    groups.append([pos])
def addAnotherGroup(groups, pos1,pos2):
    groups.append([pos1,pos2])

def  board_find_groups(board):
    lines=lines(board)
    columns=columns(board)
    board_groups=[]
    visited_board= board
    stack=[]
    in_group_board=[]
    for i in range(lines):
        for j in range(columns):
            visited_board[i][j]=0
            in_group_board[i][j]=False
    stack.append(make_pos(0,0))
    while stack!=[]:
        pos=stack.pop()
        for new_pos in getAdjacents(pos):
            if getColor(t,new_pos)==getColor(t,pos):
                if in_group_board[pos_l(new_pos)][pos_c(new_pos)]:
                    if in_group_board[pos_l(new_pos)][pos_c(new_pos)]
                    #if pos nao esta no board group:
                        addAnotherGroup(board_groups,pos,newpos)











"""def  board_find_groups(board):
    board_groups=[]
    for i in range(lines(board)):
        for j in range(columns(board)):
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
    return board_groups"""




print(board_find_groups(t))



"""class Same_game(Problem):
    def __init__(self):
        MySuperClass.__init__(self)"""
