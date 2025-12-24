using System;
using System.Collections.Generic;

namespace BiquadraticEquation {
    class Program {
        static double GetCoefficient(int index, string prompt, string[] args) {
            try {
                if (index < args.Length) {
                    return Convert.ToDouble(args[index]);
                }
            }
            catch (IndexOutOfRangeException) { }
            catch (FormatException) { }
            
            Console.Write(prompt);
            string coefStr = Console.ReadLine();
            return Convert.ToDouble(coefStr);
        }

        static List<double> GetRoots(double a, double b, double c) {
            List<double> result = new List<double>();
            
            
            double D = b * b - 4 * a * c;
            
            // для сравнения даблов
            const double eps = 1e-12;
            
            if (Math.Abs(D) < eps) {
                double y = -b / (2.0 * a);
                if (Math.Abs(y) < eps) {
                    result.Add(0.0);
                }
                else if (y > 0.0) {
                    double root = Math.Sqrt(y);
                    result.Add(root);
                    result.Add(-root);
                }
            }
            else if (D > 0.0) {
                double sqrtD = Math.Sqrt(D);
                double y1 = (-b + sqrtD) / (2.0 * a);
                double y2 = (-b - sqrtD) / (2.0 * a);
                
                if (Math.Abs(y1) < eps) { //
                    result.Add(0.0);
                }
                else if (y1 > 0.0) {
                    double root1 = Math.Sqrt(y1);
                    result.Add(root1);
                    result.Add(-root1);
                }
                
                if (Math.Abs(y2) < eps) { //
                    if (!result.Contains(0.0))
                    {
                        result.Add(0.0);
                    }
                }
                else if (y2 > 0.0) {
                    double root2 = Math.Sqrt(y2);
                    result.Add(root2);
                    result.Add(-root2);
                }
            }
            
            return result;
        }

        static void Main(string[] args) {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            
            double a = GetCoefficient(0, "Введите коэффициент A: ", args);
            double b = GetCoefficient(1, "Введите коэффициент B: ", args);
            double c = GetCoefficient(2, "Введите коэффициент C: ", args);
            
            List<double> roots = GetRoots(a, b, c);
            
            roots.Sort();
            
            int lenRoots = roots.Count;
            if (lenRoots == 0) {
                Console.WriteLine("Нет действительных корней");
            }
            else if (lenRoots == 1) {
                Console.WriteLine($"Один корень: {roots[0]}");
            }
            else if (lenRoots == 2) {
                Console.WriteLine($"Два корня: {roots[0]} и {roots[1]}");
            }
            else if (lenRoots == 3) {
                Console.WriteLine($"Три корня: {roots[0]}, {roots[1]} и {roots[2]}");
            }
            else if (lenRoots == 4) {
                Console.WriteLine($"Четыре корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}");
            }
            Console.ReadKey();
        }
    }
}
