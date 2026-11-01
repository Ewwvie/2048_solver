
import subprocess

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
    line = process.stdout.readline()

    if not line:
        return None

    if line.strip() == "over":
        return None

    board_nums = [int(i) for i in line.split()]

    if len(board_nums) != 16:
        raise ValueError("Invalid board received")

    board = [
        board_nums[j:j+4]
        for j in range(0, 16, 4)
    ]

    return board


def main():
    process = start()

    try:
        while True:
            board = get_board(process)

            if board is None:
                print("Over")
                break

            print("Board:")
            for row in board:
                print(row)

            direction = input("Enter move: ").lower()

            process.stdin.write(direction + "\n")
            process.stdin.flush()

    finally:
        if process.poll() is None:
            process.terminate()

        process.wait()


if __name__ == "__main__":
    main()
