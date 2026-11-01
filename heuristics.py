import math

weights={
    "emptiness": 270,
    "mono": 47,
    "smoothness":11,
    "merging":700
}

def  log_B2(tile):
    if tile==0:
     return 0
    return math.log2(tile)

def emptiness(board):
    return sum(
        1
        for row in board 
        for tile in row 
        if tile==0
    )
    
def mono (board):
     def penalty(line):
         x=0
         y=0
         
         for i in range(3)
         a= log_B2(line[i])
         b=log_B2(line[i+1])
         
         if a>b:
             x+=a-b
         else:
             y+=b-a
         return -min(x,y)
     score = 0 
     for row in board:
       score+=penalty(row)


for col in range (4):
    column = [board[row][col] for row in range(4)]
    score += penalty(column)
return score
        