using System;

namespace lab_6.LabOop {
    public class Circle : GeometricFigure {
        private double radius;
        private Color color;

        public override string FigureName { get; } = "Круг";

        private const double PI = Math.PI;

        public Circle(double radius, string color) {
            if (radius <= 0)
                throw new ArgumentException("Радиус должен быть положительным числом");

            this.radius = radius;
            this.color = new Color(color);
        }

        public double Radius {
            get { return radius; }
        }

        public string FigureColor {
            get { return color.ColorName; }
        }

        public override double CalculateArea() {
            return PI * radius * radius;
        }

        public override string Repr() {
            return $"Фигура: {FigureName}, радиус: {radius:F2}, цвет: {color}, площадь: {CalculateArea():F2}";
        }

        public override string ToString() {
            return Repr();
        }
    }
}