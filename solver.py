from game import get_moves
from Expectimax import expectimax

def best_move(board,d=3):
    moves=get_moves(board)

    if not moves:
        return None
    best_direction=None
    best_score=float('-inf')

    for direction,new_board in moves.items():
        score=expectimax(new_board,d-1,False)

        if score>best_score:
            best_score=score
            best_direction=direction

    return best_direction