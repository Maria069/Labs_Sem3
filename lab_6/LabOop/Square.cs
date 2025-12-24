using System;

namespace lab_6.LabOop {
    public class Square : Rectangle {
        public override string FigureName { get; } = "Квадрат";

        public Square(double side, string color) : base(side, side, color) {
        }

        public double Side {
            get { return Width; }
        }

        public override string Repr() {
            return $"Фигура: {FigureName}, сторона: {Side:F2}, цвет: {FigureColor}, площадь: {CalculateArea():F2}";
        }

        public override string ToString() {
            return Repr();
        }
    }
}