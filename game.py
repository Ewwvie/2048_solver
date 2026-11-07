def move_left(board):
    new_board = []
    for row in board:
        tiles =[x for x in row if x!=0]
        result =[]
        i=0

        while i<len(tiles):
            if i+1 <len(tiles) and tiles[i]==tiles[i+1]:
                result.append(tiles[i]*2)
                i+=2
            else:
                result.append(tiles[i])
                i+=1

        result+=[0]*(4 - len(result))
        new_board.append(result)
    return new_board


def move_right(board):
    new_board=[]
    for row in board:
        tiles=[x for x in row if x!=0]
        result=[]
        i=len(tiles)-1
        while i>=0:
            if i-1>=0 and tiles[i]==tiles[i-1]:
                result.append(tiles[i]*2)
                i-=2
            else:
                result.append(tiles[i])
                i-=1

        result +=[0] * (4-len(result))
        result.reverse()
        new_board.append(result)

    return new_board


def move_up(board):
    new_board=[[0]*4for _ in range(4)]

    for c in range(4):
        tiles=[]
        for r in range(4):
            if board[r][c]!=0:
                tiles.append(board[r][c])

        result=[]
        i=0
        while i < len(tiles):
            if i+1 <len(tiles) and tiles[i]==tiles[i+1]:
                result.append(tiles[i]*2)
                i+=2
            else:
                result.append(tiles[i])
                i+=1

        for r in range(len(result)):
            new_board[r][c]=result[r]

    return new_board


def move_down(board):
    new_board =[[0]*4 for _ in range(4)]

    for c in range(4):
        tiles=[]

        for r in range(4):
            if board[r][c]!= 0:
                tiles.append(board[r][c])

        result=[]
        i=len(tiles)-1

        while i>=0:
            if i-1>=0 and tiles[i]==tiles[i-1]:
                result.append(tiles[i]*2)
                i-=2
            else:
                result.append(tiles[i])
                i-=1

        for r in range(len(result)):
            new_board[3-r][c]=result[r]

    return new_board


def move(board, direction):
    if direction=="left":
        new_board=move_left(board)
    elif direction=="right":
        new_board=move_right(board)
    elif direction=="up":
        new_board=move_up(board)
    elif direction=="down":
        new_board=move_down(board)
    else:
        raise ValueError("Invalid direction")

    changed =(new_board!=board)
    return new_board,changed


def get_moves(board):
    directions = ["left","right","up","down"]
    moves={}

    for direction in directions:
        new_board,changed =move(board, direction)

        if changed:
            moves[direction]=new_board

    return moves

def get_state(board):
 empty=[]
 for i in range(4):
    for j in range (4):
       if board[i][j]==0:
        empty.append((i,j))
 if not empty:
     return[
     ]
 states=[
 ]
 n=len(empty)
 for i,j in empty:
     board2=[row[:] for row in board]
     board2[i][j]=2
     states.append((.9/n,board2))
     
     board4=[row[:] for row in board]
     board4[i][j]=4
     states.append((0.1/n,board4))
     
 return states 
 