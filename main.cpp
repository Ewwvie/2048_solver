
#include <iostream>

#include "Board.h"

using namespace std;

int main() {
    Board board;
    cout << "Initial board:\n";
    board.print();
    cout << "\nEmpty cells: "
         << board.noEmpty() << '\n';
    return 0;
}
