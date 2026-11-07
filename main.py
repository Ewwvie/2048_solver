import subprocess
from game import get_state,get_moves
from solver import best_move
def start():
    process = subprocess.Popen(
        ["./solver"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    return process

def get_board(process):
    line=process.stdout.readline()
    
    if not line:
        return None, None
    line =line.strip()
     
    if line.startswith("over"):
         parts=line.split()
         score=int(parts[1]) if len(parts)>1 else 0
         return None,score

    board_nums= [int(i) for i in line.split()]
    board=[
        board_nums[j:j+4]
        for j in range(0,16,4)
    ]
    
    score_line=process.stdout.readline().strip()
    
    if not score_line.startswith("score "):
        raise ValueError(f"Expected score line, received: {score_line}")
    score=int(score_line.split()[1])
    return board,score

def print_board(board):
    print("\n"+"-"*25)
    for row in board:
        print("|".join(f"{x:^5}" if x else "  .  " for x in row))
    print("-"*25)

def main():
    process=start()
    
    try:
        while True:
            board,score=get_board(process)
            
            if board is None:
             print("Over")
             break
            print("Score:",score)
            print_board(board)
            dir=best_move(board,3)
        
            if dir is None:
             break
        
            process.stdin.write(dir+"\n")
            process.stdin.flush()
        
        
    finally:
        if process.poll() is None:
            process.terminate()
        process.wait()
        
if __name__ == "__main__":
    main()