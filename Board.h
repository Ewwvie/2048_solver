
#ifndef BOARD_H
#define BOARD_H

#include <random>
#include <string>
class Board {
private:
    int cells[4][4];
    std::mt19937 rng;
    bool moveLeft();
    bool moveRight();
    bool moveUp();
    bool moveDown();
public:
    Board();
    void print() const;
    int noEmpty() const;
    void makeTile();

    bool move(std::string & direction){
        if(direction=="left") return moveLeft();
        if(direction=="right") return moveRight();
        if(direction=="up") return moveUp();
        if(direction=="down") return moveDown();
        return false;
    }
    bool isOver() const;
    int getPoints() const;
    void sendBoard() const;
};

#endif
