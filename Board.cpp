
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


//moving right
bool Board:: moveRight(){
 bool changed = false;
 for(int i=0; i<4; i++){
    //removing zeros
    vector<int>x;
for(int j=3;j>=0;j--){
    if(cells[i][j]){
        x.push_back(cells[i][j]);
    }
}
//tiles after merging 
vector<int> y;
int j = 0;
 while (j<x.size()) {
    if ((j + 1) < x.size() &&
        x[j] == x[j +1]) {
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
    if(cells[i][3-j] !=y[j]){
        changed=true;
    }
    cells[i][3-j] = y[j];
}

}
return changed;
}

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
//moving up
bool Board::moveUp() {
    bool changed = false;

    for (int j = 0; j < 4; j++) {
        // removing zeros
        vector<int> x;

        for (int i = 0; i < 4; i++) {
            if (cells[i][j]) {
                x.push_back(cells[i][j]);
            }
        }

        // tiles after merging
        vector<int> y;
        int i = 0;

        while (i < x.size()) {
            if ((i + 1) < x.size() &&
                x[i] == x[i + 1]) {
                y.push_back(x[i] * 2);
                i += 2;
            }
            else {
                y.push_back(x[i]);
                i++;
            }
        }

        while (y.size() < 4) {
            y.push_back(0);
        }

        for (int i = 0; i < 4; i++) {
            if (cells[i][j] != y[i]) {
                changed = true;
            }
            cells[i][j] = y[i];
        }
    }

    return changed;
}

//moving down
bool Board::moveDown() {
    bool changed = false;

    for (int j = 0; j < 4; j++) {
        // removing zeros
        vector<int> x;

        for (int i = 3; i >= 0; i--) {
            if (cells[i][j]) {
                x.push_back(cells[i][j]);
            }
        }

        // tiles after merging
        vector<int> y;
        int i = 0;

        while (i < x.size()) {
            if ((i + 1) < x.size() &&
                x[i] == x[i + 1]) {
                y.push_back(x[i] * 2);
                i += 2;
            }
            else {
                y.push_back(x[i]);
                i++;
            }
        }

        while (y.size() < 4) {
            y.push_back(0);
        }

        for (int i = 0; i < 4; i++) {
            if (cells[3 - i][j] != y[i]) {
                changed = true;
            }
            cells[3 - i][j] = y[i];
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

bool Board::isOver() const{
if(noEmpty()){
    return false;
}
 
for(int i=0;i<4;i++){
    for(int j=0; j<4;j++){
        if(j<3 && cells[i][j]==cells[i][j+1]){
            return false;
        }
        if(i<3 && cells[i][j]==cells[i+1][j] ){
            return false;
        }
    }
}
return true;
}


