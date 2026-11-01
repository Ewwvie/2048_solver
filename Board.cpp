
#include "Board.h"
#include <iostream>
#include <vector>
#include <utility>
#include <cstdlib>
#include <random>
using namespace std;
Board::Board() : rng(random_device{}()) {
    for(int i=0; i<4;i++){
        for(int j=0 ; j<4;j++){
            cells[i][j]=0;

        }
    }
    makeTile();
    makeTile();

}
void Board::print() const {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << cells[i][j] << " ";
        }
        cout << '\n';
    }
}
int Board::noEmpty() const {
    int sol = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (cells[i][j] == 0) {
                sol++;
            }
        }
    }
    return sol;
}


//moving left
bool Board:: moveLeft(){
 bool changed = false;
 for(int i=0; i<4; i++){
    //removing zeros
    vector<int>x;
for(int j=0;j<4;j++){
    if(cells[i][j]){
        x.push_back(cells[i][j]);
    }
}
//tiles after merging 
vector<int> y;
int j = 0;
 while (j < x.size()) {
    if ((j + 1) < x.size() &&
        x[j] == x[j + 1]) {
        y.push_back(x[j] * 2);
            j += 2;
        }
            else {
            y.push_back(x[j]);
                j++;
            }
}
while(y.size()<4){
    y.push_back(0);
}
for(int j=0;j<4;j++){
    if(cells[i][j] !=y[j]){
        changed=true;
    }
    cells[i][j] = y[j];
}

}
return changed;
}




void Board::makeTile() {
vector<pair<int,int>> emptyCells;
for(int i=0; i<4; i++){
    for(int j =0; j<4; j++){
        if(cells[i][j]==0){
            emptyCells.push_back({i,j});
        }
    }}
    if(emptyCells.empty()) return ;

    uniform_int_distribution<size_t> distri(0,emptyCells.size()-1);
    uniform_int_distribution<int> valOfdistri(1,10);

    auto[row,column] = emptyCells[distri(rng)];
    if(valOfdistri(rng)==10) cells[row][column] =4;
    else cells[row][column]=2;
    

}
