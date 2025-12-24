#include <iostream>
#include <vector>
#include <memory>
#include "MyOop/Rectangle.h"
#include "MyOop/Circle.h"
#include "MyOop/Square.h"

using namespace std;

// вариантт
const int N = 11;

int main() {

    vector<unique_ptr<GeometricFigure>> figures;
    
    figures.push_back(make_unique<Rectangle>(N, N, "синий"));
    figures.push_back(make_unique<Circle>(N, "зеленый"));
    figures.push_back(make_unique<Square>(N, "красный"));
    
    for (const auto& figure : figures) {
        cout << figure->repr() << endl;
    }
        
    return 0;
}
