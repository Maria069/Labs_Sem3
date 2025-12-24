#pragma once
#include <string>
#include "Rectangle.h"

class Square : public Rectangle {
private:
    static const std::string figureName;

public:
    Square(double side, const std::string& color);
    
    double getSide() const { return getWidth(); }
    
    std::string getFigureName() const override;
    std::string repr() const override;
};
