using System;

namespace lab_6.LabOop {
    public abstract class GeometricFigure {
        public virtual string FigureName { get; } = "Геометрическая фигура";

        public abstract double CalculateArea();

        public abstract string Repr();
    }
}