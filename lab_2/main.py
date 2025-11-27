from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

N = 11

def main():
    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")
    
    print(rectangle)
    print(circle)
    print(square)
    
    figures = [rectangle, circle, square]
    print("\nВсе фигуры:")
    for figure in figures:
        print(f"  - {figure.getName()}: площадь = {figure.area():.2f}")

if __name__ == "__main__":
    main()