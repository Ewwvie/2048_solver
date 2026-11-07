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
        return None
    if line.strip()=="over":
        return None
    
    board_nums= [int(i) for i in line.split()]
    board=[
        board_nums[j:j+4]
        for j in range(0,16,4)
    ]
    return board

def main():
    process=start()
    
    try:
        while True:
            board=get_board(process)
            
            if board is None:
             print("Over")
             break
        
            dir=best_move(board,3)
        
            if dir is None:
             break
        
            print(dir)
            process.stdin.write(dir+"\n")
            process.stdin.flush()
        
        
    finally:
        if process.poll() is None:
            process.terminate()
        process.wait()
        
if __name__ == "__main__":
    main()