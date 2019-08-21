#ifndef DICESIDE_H
#define DICESIDE_H

#include <iosfwd>
#include <string>
#include <stdexcept>
#include <sstream>
#include <iomanip>


class Dice_side
{
public:
    Dice_side(std::string image_path, int value): image_path{image_path}, value{value} {};

    ~Dice_side() = default;

    int get_value() const
    {
        return value;
    }

    std::string get_image() const
    {
        return image_path;
    }


private:
    int value;
    std::string image_path;

};

#endif // DICESIDE_H

