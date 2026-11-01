
#include <iostream>

#include "Board.h"

using namespace std;

int main() {
    Board board;
    string direction;

    while (true) {
        if (board.isOver()) {
            cout << "over" << endl;
            break;
        }
        board.sendBoard();
        if (!(cin >> direction)) {
            break;
        }

        if (board.move(direction)) {
            board.makeTile();
        }
    }

    return 0;
}
