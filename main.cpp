
#include <iostream>

#include "Board.h"

using namespace std;

int main() {
    Board board;
    string direction;
    while(!board.isOver()){
    cout << "Initial board:\n";
    board.print();
    cout << "\n enter direction";
    cin>> direction;
    cout << "\nEmpty cells: "
        << board.noEmpty() << '\n';
      if (board.move(direction)) {
            board.makeTile();
        }
        else {
            cout << "Invalid move! Try again.\n";
        }
     
    }
        board.print();
        cout<<"over";

    return 0;
}
