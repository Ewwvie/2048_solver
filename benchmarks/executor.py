import argparse #to accept command line argyments
import os #check the existence of the executable 
import re #Extract numbers from output using regular expressions
import subprocess #interact with cpp
import time

from solver import best_move
from benchmarks.metrics import save_results

def read_state(process):
    line=process.stdout.readline()
    
    if not line:
        raise RuntimeError("Game engine terminated")
    line=line.strip()

    if line.startswith("over"):
        match = re.search(r"over\s+(\d+)", line) #capturing score
        if match:
         score = int(match.group(1))
        else:
         score = 0
        return None, score

    board_values = list(map(int,line.split()))

    board = [
        board_values[i:i + 4]
        for i in range(0, 16, 4)
    ]

    score_line=process.stdout.readline().strip()
    match = re.search(r"score\s+(\d+)", score_line)

    if not match:
        raise RuntimeError(f"Invalid score received: {score_line}")

    return board, int(match.group(1))


def run(engine, depth):
    start=time.perf_counter() #innitalising the time i am recording
    latencies=[] #time taken per move
    moves = 0
    process = subprocess.Popen(
        [engine],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        bufsize=1
    )

    try:
        board, score = read_state(process)
        while board is not None:
            start = time.perf_counter()

            direction = best_move(board, depth)

            end = time.perf_counter()
            latencies.append(end - start)

            if direction is None:
                break
            process.stdin.write(direction + "\n")
            process.stdin.flush()
            moves += 1
            board, score = read_state(process)
        duration = time.perf_counter() - start
        max_tile = max(max(row) for row in board) if board else 0

        return {
            "score": score,
            "max_tile": max_tile,
            "moves": moves,
            "duration": duration,
            "average_latency": (
                sum(latencies) / len(latencies) * 1000
                if latencies else 0
            )
        }, latencies

    finally:
        if process.poll() is None:
            process.terminate()
            process.wait()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--games",type=int,default=100)
    parser.add_argument("--depth",type=int,default=3)
    parser.add_argument("--engine",default="./solver")
    args = parser.parse_args()

    if not os.path.exists(args.engine):
        raise FileNotFoundError(
            f"Engine not found: {args.engine}.compile first"
        )

    results=[]
    all_latencies=[]

    for i in range(args.games):
        print(f"Running game {i + 1}/{args.games}...", end=" ")
        result, latencies = run(args.engine, args.depth)
        results.append(result)
        all_latencies.extend(latencies)
        print(
            f"Score: {result['score']} | "
            f"Moves: {result['moves']} | "
            f"Time: {result['duration']:.2f}s"
        )
    save_results(results,all_latencies,args.depth)


if __name__ == "__main__":
    main()
