#include "Square.h"

const std::string Square::figureName = "Квадрат";

Square::Square(double side, const std::string& color) 
    : Rectangle(side, side, color) {}

std::string Square::getFigureName() const {
    return figureName;
}

std::string Square::repr() const {
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2);
    oss << "Фигура: " << figureName 
        << ", сторона: " << getSide() 
        << ", цвет: " << getColor() 
        << ", площадь: " << area();
    return oss.str();
}