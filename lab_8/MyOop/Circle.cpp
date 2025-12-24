#include "Circle.h"
#include <cmath>

// gjkttt
const std::string Circle::figureName = "Круг";

Circle::Circle(double radius, const std::string& color) 
    : radius(radius), color(color) {
    if (radius <= 0) {
        throw std::invalid_argument("Радиус должен быть положительным числом");
    }
}

double Circle::area() const {
    return M_PI * radius * radius;
}

std::string Circle::getFigureName() const {
    return figureName;
}

std::string Circle::repr() const {
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2);
    oss << "Фигура: " << figureName 
        << ", радиус: " << radius 
        << ", цвет: " << color.getColor() 
        << ", площадь: " << area();
    return oss.str();
}