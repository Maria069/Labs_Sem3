#pragma once
#include <string>
#include <sstream>
#include <iomanip>
#include "GeometricFigure.h"
#include "Color.h"

class Rectangle : public GeometricFigure {
protected:
    double width;
    double height;
    Color color;
    static const std::string figureName;

public:
    Rectangle(double width, double height, const std::string& color);
    
    double getWidth() const { return width; }
    double getHeight() const { return height; }
    std::string getColor() const { return color.getColor(); }
    
    double area() const override;
    std::string getFigureName() const override;
    std::string repr() const override;
};
