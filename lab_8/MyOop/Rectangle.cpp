#include "Rectangle.h"

// вот это стат поле не забыть
const std::string Rectangle::figureName = "Прямоугольник";

Rectangle::Rectangle(double width, double height, const std::string& color) 
    : width(width), height(height), color(color) {
    if (width <= 0 || height <= 0) {
        throw std::invalid_argument("Ширина и высота !< 0");
    }
}

double Rectangle::area() const {
    return width * height;
}

std::string Rectangle::getFigureName() const {
    return figureName;
}

// вывод не забыть
std::string Rectangle::repr() const {
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2);
    oss << "Фигура: " << figureName 
        << ", ширина: " << width 
        << ", высота: " << height 
        << ", цвет: " << color.getColor() 
        << ", площадь: " << area();
    return oss.str();
}