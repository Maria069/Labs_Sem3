#pragma once
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include "GeometricFigure.h"
#include "Color.h"

class Circle : public GeometricFigure {
private:
    double radius;
    Color color;
    static const std::string figureName;

public:
    Circle(double radius, const std::string& color);
    
    double getRadius() const { return radius; }
    std::string getColor() const { return color.getColor(); }
    
    double area() const override;
    std::string getFigureName() const override;
    std::string repr() const override;
};
