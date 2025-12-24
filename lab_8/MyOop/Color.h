#pragma once
#include <iostream>
#include <string>

class Color {
private:
    std::string color;

public:
    Color(const std::string& color = "") : color(color) {}
    
    std::string getColor() const { return color; }
    
    void setColor(const std::string& newColor) { color = newColor; }
    
    operator std::string() const { return color; }
    
    std::string toString() const { return color; }
};
