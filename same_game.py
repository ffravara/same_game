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
    t[pos_l(pos)][pos_c(pos)]=get_no_color()
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
    i=GetGroupIndex(groups,pos1)
    print(i)
    j=GetGroupIndex(groups,pos2)
    print(j)
    new_list=copy.deepcopy(groups[i])

    if (i!=j):
        for el in groups[j]:
            new_list.append(el)
        del groups[i]
        del groups[j-1]
        groups.append(new_list)


def visited(visited_board,pos):
    return visited_board[pos_l(pos)][pos_c(pos)]==2
def partlyVisited(visited_board,pos):
    return visited_board[pos_l(pos)][pos_c(pos)]==1
def setVisited(visited_board,pos):
    visited_board[pos_l(pos)][pos_c(pos)]=2
def setpartlyVisited(visited_board,pos):
    visited_board[pos_l(pos)][pos_c(pos)]=1





groups=[]

def  board_find_groups(board):

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

        print ("This the current ball: {}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format(currentBall))
        for adjacentBall in getAdjacents(board,currentBall):
            print(adjacentBall)
            if currentBall==(3,4):#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                print(stack)
            #primeiro, vemos se adJacentBall já foi visitado
            if visited(visited_board,adjacentBall):
                print("adjacente tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                if getColor(t,adjacentBall)==getColor(t,currentBall):
                    #segundo, ver se currentBall tem grupo
                    if currentBall_in_group:
                        #juntar grupos da duas bolas
                        print("current tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        appendGroups(groups,currentBall,adjacentBall)
                    else:
                        #currentBall nao tem grupo, entao juntamo-la ao grupo da adjacente
                        print("current  NAO tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        addToGroup(groups,GetGroupIndex(groups,adjacentBall),currentBall)
                        nowInGroup(groupBoard,currentBall)
                        currentBall_in_group=True

            #Se a adjacentBall ainda nao foi visitada

            else:
                if getColor(t,adjacentBall)==getColor(t,currentBall):
                    if currentBall_in_group:
                        #se a currentBall ja tem grupo e a adjacentBall tambem, juntamo-los
                        print("current tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        if inGroup(groupBoard, adjacentBall):
                            #juntamos os grupos
                            print("adjacente tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                            appendGroups(groups,currentBall,adjacentBall)
                        else:
                            #metemos a adjacente no grupo da currentBall
                            print("adjacente NAO tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                            addToGroup(groups,GetGroupIndex(groups,currentBall),adjacentBall)
                            nowInGroup(groupBoard,adjacentBall)
                    #se a currentBall ainda nao tem grupo...
                    else:
                        #e a adjacentBall tiver grupo... juntamo-los
                        if inGroup(groupBoard, adjacentBall):
                            print("adjacente tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                            appendGroups(groups,currentBall,adjacentBall)
                            nowInGroup(groupBoard, currentBall)
                        #nenhuma tem grupo
                        else:
                            print("nenhuma tem grupo")#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                            addTwoGroup(groups, currentBall, adjacentBall)
                            currentBall_in_group=True
                            nowInGroup(groupBoard,adjacentBall)
                            nowInGroup(groupBoard,currentBall)
                if not partlyVisited(visited_board, adjacentBall):
                    stack.append(adjacentBall)
                setpartlyVisited(visited_board, adjacentBall)
            if currentBall_in_group==False:
                addAnotherGroup(groups,currentBall)
                currentBall_in_group=True
        setVisited(visited_board,currentBall)
        print(groups)
    return groups
"""
#print(board_find_groups(t))
def board_remove_groups(t, group):
    board=copy.deepcopy(t)
    lines=seeLines(board)
    columns=seeLines(board)
    for sublist in groups:
        if group==sublist:
            for ball in sublist:
                set_no_color(board, ball)
    index=0
    for j in range(columns):
        for i in range(lines, -1, -1):
            if has_no_color(board,make_pos(i,j)):
                index=i-1
                #empurra os de cima desse para baixo
                for k in range(index,-1,-1):
                    color=getColor(board, make_pos(index,j))
                    setColor(board, make_pos(index+1,j),color)




    for j in range(columns,-1-1):
        for i in range(lines, -1, -1):
            if has_no_color(board,make_pos(i,j)):
                for k in range(i)
                    color=getColor(board, make_pos(i,j), color)


"""




t=[[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]
printBoard(t)
print(board_find_groups(t))





"""GREEN TRASH (hopefully not needed recyclabe shit)"""




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
