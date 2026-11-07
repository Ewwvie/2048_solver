import math
from functools import lru_cache
weights={
    "emptiness": 270,
    "mono": 47,
    "smoothness":11,
    "merging":700
}
@lru_cache(maxsize=None)
def  log_B2(tile):
    if tile==0:
     return 0
    return math.log2(tile)

def emptiness(board):
    return sum(tile==0 for row in board for tile in row)
    
def mono (board):
     def penalty(line):
         x=0
         y=0
         
         for i in range(3):
            a=log_B2(line[i])
            b=log_B2(line[i+1])
            if a>b:
                x+=a-b
            else:
                y+=b-a
         return -min(x,y)
     score=0
    
     for row in board:
       score+=penalty(row)


     for col in range (4):
      column = [board[row][col] for row in range(4)]
      score += penalty(column)
     return score
 
def smoothness(board):
    score = 0
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                continue
            current = log_B2(board[r][c])
            if c < 3 and board[r][c + 1] != 0:
                neighbour = log_B2(board[r][c + 1])
                score -= abs(current - neighbour)
            if r < 3 and board[r + 1][c] != 0:
                neighbour = log_B2(board[r + 1][c])
                score -= abs(current - neighbour)
    return score


def merging(board):
    score = 0
    for r in range(4):
        for c in range(4):
            current = board[r][c]
            if current == 0:
                continue
            if c < 3 and board[r][c + 1] == current:
                score += log_B2(current)
            if r < 3 and board[r + 1][c] == current:
                score += log_B2(current)

    return score

def evaluate(board):
    sum = (
        weights["emptiness"] * emptiness(board)
        + weights["mono"] * mono(board)
        + weights["smoothness"] * smoothness(board)
        + weights["merging"] * merging(board)
    )
    return sum


def breakdown(board):
    return {
        "emptiness": weights["emptiness"] * emptiness(board),
        "monotonicity": weights["mono"] * mono(board),
        "smoothness": weights["smoothness"] * smoothness(board),
        "merging": weights["merging"] * merging(board),
        "total": evaluate(board)
    }