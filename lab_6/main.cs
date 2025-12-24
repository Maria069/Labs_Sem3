using System;
using System.Collections.Generic;
using lab_6.LabOop;

namespace lab_6 {
    class Program {
        static void Main(string[] args) {
            const int n = 11;
            List<GeometricFigure> figures = new List<GeometricFigure> {
                new Rectangle(n, n, "синий"),
                new Circle(n, "зеленый"),
                new Square(n, "красный"),
            };

            foreach (var figure in figures) {
                Console.WriteLine(figure.Repr());
            }
            Console.ReadKey();
        }
    }
}