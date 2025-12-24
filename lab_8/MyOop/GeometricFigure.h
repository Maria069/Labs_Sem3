#pragma once
#include <iostream>
#include <string>

class GeometricFigure {
public:
    virtual ~GeometricFigure() {}
    
    virtual double area() const = 0;
    
    virtual std::string getFigureName() const = 0;
    
    virtual std::string repr() const = 0;
};
