
visited = [[False for i in range(5)]for j in range(5)]

def printBoard(t):
    i=0
    j=0
    for i in range(lines(t)):
        print( getLine(t,i))

print(visited)
