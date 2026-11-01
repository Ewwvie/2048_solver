
/*#include <iostream>
#include <vector>
#include <utility>
#include <cstdlib>
#include <ctime>
using namespace std;

void spawnTile(int board[4][4]) {
    vector<pair<int, int>> emptyCells;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == 0) {
                emptyCells.push_back({i, j});
            }
        }
    }
    if (emptyCells.empty()) {
        return;
    }
    int index = rand() % emptyCells.size();
    int row = emptyCells[index].first;
    int col = emptyCells[index].second;
    int value = (rand() % 10 == 9) ? 4 : 2;

    board[row][col] = value;
}
int main() {
    srand(time(0));

    int board[4][4] = {
        {2, 0, 4, 0},
        {0, 8, 0, 0},
        {2, 2, 0, 0},
        {0, 0, 16, 0}
    };
    int emptyCount = 0;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == 0) {
                emptyCount++;
            }
        }
    }
    cout << "Empty cells before spawning: "
         << emptyCount << "\n";
    spawnTile(board);
    cout << "Board after spawning:\n";
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << board[i][j] << "\t";
        }
        cout << "\n";
    }
    return 0;
}
