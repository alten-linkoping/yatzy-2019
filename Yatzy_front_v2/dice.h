#ifndef DICE_H
#define DICE_H

#include <iosfwd>
#include <string>
#include <stdexcept>
#include <iomanip>
#include "dice_side.h"

class Dice
{
public:
    Dice(Dice_side& Side_up);
    ~Dice() = default;


    void set_side_up(Dice_side& new_side_up)
    {
        Side_up = new_side_up;
    }

    Dice_side& get_side_up()
    {
        return Side_up;
    }
private:
    Dice_side& Side_up;
};


#endif // DICE_H
