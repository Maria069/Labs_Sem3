using System;

namespace lab_6.LabOop {
    public class Rectangle : GeometricFigure {
        private double width;
        private double height;
        private Color color;

        public override string FigureName { get; } = "Прямоугольник";

        public Rectangle(double width, double height, string color) {
            if (width <= 0 || height <= 0)
                throw new ArgumentException("Ширина и высота должны быть положительными числами");

            this.width = width;
            this.height = height;
            this.color = new Color(color);
        }

        public double Width {
            get { return width; }
        }

        public double Height {
            get { return height; }
        }

        public string FigureColor {
            get { return color.ColorName; }
        }

        public override double CalculateArea() {
            return width * height;
        }

        public override string Repr() {
            return $"Фигура: {FigureName}, ширина: {width:F2}, высота: {height:F2}, цвет: {color}, площадь: {CalculateArea():F2}";
        }

        public override string ToString() {
            return Repr();
        }
    }
}