import copy

"""TAD board"""

def seeLines(t):
    return len(t)
def seeColumns(t):
    return len(t[0])
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
        return pos_c(source)<columns-1


def getAdjacents(t,pos):
    adjacents=[]
    if valid_move(t,pos,'u'):
        adjacents.append(make_pos(pos_l(pos)-1, pos_c(pos)))
    if valid_move(t,pos,'d'):
        adjacents.append(make_pos(pos_l(pos)+1, pos_c(pos)))
    if valid_move(t,pos,'l'):
        adjacents.append(make_pos(pos_l(pos), pos_c(pos)-1))
    if valid_move(t,pos,'r'):
        adjacents.append(make_pos(pos_l(pos), pos_c(pos)+1))


    return adjacents



"""TAI color"""
# sem cor = 0
# com cor > 0
def get_no_color():
    return 0
def set_no_color(t,pos):
    t[pos_l(pos)][pos_c(pos)]=0
def no_color (c):
    return c==0
def color (c):
    return c > 0
def getColor( t ,pos):
    return t[pos_l(pos)][pos_c(pos)]
def has_no_color(t,pos):
    return t[pos_l(pos)][pos_c(pos)]==get_no_color()
def has_color(t,pos):
    return t[pos_l(pos)][pos_c(pos)]>0
def setColor(t,pos,color):
        t[pos_l(pos)][pos_c(pos)]=color




"""TAD group"""

def addToGroup(g,i,pos):
    g[i].append(pos)
def addAnotherGroup(groups,pos):
    groups.append([pos])
def addTwoGroup(groups, pos1,pos2):
    groups.append([pos1,pos2])



def GetGroupIndex(groups,pos):
    index = -1
    for sublist in groups:
        index=index + 1
        if pos in sublist:
            return index


def inGroup(groupBoard, pos):
    return groupBoard[pos_l(pos)][pos_c(pos)]
def nowInGroup(groupBoard,pos):
    groupBoard[pos_l(pos)][pos_c(pos)]=True

def appendGroups(groups,pos1,pos2):
    j=GetGroupIndex(groups,pos1)
    i=GetGroupIndex(groups,pos2)
    if (i!=j):

        new_list=copy.deepcopy(groups[i])

        for el in groups[j]:
            new_list.append(el)
        del groups[i]
        if i<j:
            del groups[j-1]
        else:
            del groups[j]
        groups.append(new_list)


def visited(visited_board,pos):
    return visited_board[pos_l(pos)][pos_c(pos)]==2
def partlyVisited(visited_board,pos):
    return visited_board[pos_l(pos)][pos_c(pos)]==1
def setVisited(visited_board,pos):
    visited_board[pos_l(pos)][pos_c(pos)]=2
def setpartlyVisited(visited_board,pos):
    visited_board[pos_l(pos)][pos_c(pos)]=1






def  board_find_groups(board):
    groups=[]

    lines=seeLines(board)
    columns =seeColumns(board)

    visited_board=[[0 for i in range(columns)]for j in range(lines)]
    groupBoard=[[False for i in range(columns)]for j in range(lines)]
    stack=[]

    stack.append(make_pos(0,0))


    while stack!=[]:
        currentBall = stack.pop()
        currentBall_in_group = False
        if inGroup(groupBoard, currentBall):
            currentBall_in_group=True

        for adjacentBall in getAdjacents(board,currentBall):
            #primeiro, vemos se adJacentBall já foi visitado
            if visited(visited_board,adjacentBall):
                if getColor(board,adjacentBall)==getColor(board,currentBall):
                    #segundo, ver se currentBall tem grupo
                    if currentBall_in_group:
                        #juntar grupos da duas bolas
                        appendGroups(groups,currentBall,adjacentBall)
                    else:
                        #currentBall nao tem grupo, entao juntamo-la ao grupo da adjacente
                        addToGroup(groups,GetGroupIndex(groups,adjacentBall),currentBall)
                        nowInGroup(groupBoard,currentBall)
                        currentBall_in_group=True

            #Se a adjacentBall ainda nao foi visitada

            else:
                if getColor(board,adjacentBall)==getColor(board,currentBall):
                    if currentBall_in_group:
                        #se a currentBall ja tem grupo e a adjacentBall tambem, juntamo-los
                        if inGroup(groupBoard, adjacentBall):
                            #juntamos os grupos
                            appendGroups(groups,currentBall,adjacentBall)
                        else:
                            #metemos a adjacente no grupo da currentBall
                            addToGroup(groups,GetGroupIndex(groups,currentBall),adjacentBall)
                            nowInGroup(groupBoard,adjacentBall)
                    #se a currentBall ainda nao tem grupo...
                    else:
                        #e a adjacentBall tiver grupo... juntamo-los
                        if inGroup(groupBoard, adjacentBall):
                            addToGroup(groups,GetGroupIndex(groups,adjacentBall),currentBall)
                            nowInGroup(groupBoard, currentBall)
                        #nenhuma tem grupo
                        else:
                            addTwoGroup(groups, currentBall, adjacentBall)
                            nowInGroup(groupBoard,adjacentBall)
                            nowInGroup(groupBoard,currentBall)
                        currentBall_in_group=True
                if not partlyVisited(visited_board, adjacentBall):
                    stack.append(adjacentBall)
                    setpartlyVisited(visited_board, adjacentBall)
        if currentBall_in_group==False:
            addAnotherGroup(groups,currentBall)
            currentBall_in_group=True
        setVisited(visited_board,currentBall)

    return groups


#print(board_find_groups(board))"""

"""def printwithgroups(l,c,groups,board):
    board=[[0 for i in range(c)]for j in range(l)]
    for sublist in groups:
        for pos in sublist:
            board[pos_l(pos)][pos_c(pos)]=getColor(t,pos)
    printBoard(board)

printwithgroups(10,4,board_find_groups(t),t)"""


def board_remove_group(t, group):

    groups = board_find_groups(t)
    board = copy.deepcopy(t)
    lines=seeLines(board)
    columns=seeColumns(board)

    groupToRemove = []
    for pos in group:
        tuplePos = make_pos(pos_l(pos), pos_c(pos))
        groupToRemove.append(tuplePos)

    #encontrar o grupo que e eliminado, e por as posicoes a zero(sem cor)
    for i in range(len(groups)):

        if set(groupToRemove) == set(groups[i]):
            for ball in groups[i]:
                set_no_color(board, ball)
            del groups[i]
            break



    boardT = list(map(list, zip(*board)))
    #COMPACTACO VERTICAL
    for i in range(len(boardT)):
        contador_zeros=0
        new_list=[]
        for ball in boardT[i]:
            if ball==get_no_color():
                contador_zeros=contador_zeros+1
            else:
                new_list.append(ball)
        new_line=[0 for i in range(contador_zeros)]
        new_line += new_list
        boardT[i]= new_line
    nrZeroLines = 0
    result = []


    #COMPACTAÇAO HORIZONTAL
    for i in range(columns):


        colunas = len(boardT[i])

        if sum(boardT[i]) != 0:
            result.append(boardT[i])
        else:
            nrZeroLines += 1


    for i in range(nrZeroLines):
        result.append([0]* lines)





    board = list(map(list, zip(*result)))
    return board


#t = [[1,1,2], [1,4,5],[1,5,5], [1,2,3]]

#printBoard(t)

#groups = board_find_groups(t)

#print(groups)

#newBoard = board_remove_group(t, [(0,0),(1,0),(2,0),(3,0),(0,1)])

#printBoard(newBoard)

#t = [[1,1,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3]]

#printBoard(t)

#print(board_remove_group([[1,1,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3]],[[0,0],[0,1]]))

#"""

#t = [[3,3,0,3,3,3],[2,2,0,3,3,3],[2,2,0,3,3,3],[2,2,1,3,3,3],[2,2,1,3,3,3]]
#printBoard(t)

#print(' ')

#printBoard(board_remove_group([[3,3,0,3,3,3],[2,2,0,3,3,3],[2,2,0,3,3,3],[2,2,1,3,3,3],[2,2,1,3,3,3]],[[4,2],[3,2]]))

"""
    for i in range(len(groups)):
        equal=True
        if len(group)!=len(groups[i]):
            esqual=False
        for element in groups:
            if element not in groups[i]:
                equal=False
        if equal==True:
            for ball in groups[i]:
                set_no_color(board, ball)
            del groups[i]


    """
