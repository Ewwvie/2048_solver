from game import get_moves , get_state
from heuristics import evaluate 

def expectimax(board,d,max):
    if d==0:
        return evaluate(board)
    if max:
        move=get_moves(board)
        if not move:
            return evaluate(board)
        best=float('-inf')
        for dir,new_board in move.items():
            value=expectimax(new_board,d,False)

            if value>best:
                best=value

        return best

    states=get_state(board)

    if not states:
        return evaluate(board)

    expected=0
    for probability,new_board in states:
        value=expectimax(new_board,d-1,True)
        expected+=probability*value

    return expected

        

def best_move(board,d=2):
    move=get_moves(board)
    if not move:
        return None
    best=-1000000
    best_dir=None
    for dir,new_board in move.items():
        value=expectimax(new_board,d,False)
        
        if value>best:
          best=value
          best_dir=dir
    return best_dir
