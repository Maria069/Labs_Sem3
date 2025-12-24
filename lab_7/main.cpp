#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

const double eps = 1e-12;

double get_coef(int index, const string& prompt, int argc, char* argv[]) {
    double coef;
    if (index < argc) {
        coef = stod(argv[index]);
    } else {
        cout << prompt;
        cin >> coef;
    }
    return coef;
}

vector<double> get_roots(double a, double b, double c) {
    vector<double> result;
    
    double D = b * b - 4 * a * c;
    
    if (abs(D) < eps) {
        double y = -b / (2.0 * a);
        if (abs(y) < eps) {
            result.push_back(0.0);
        } else if (y > 0.0) {
            double root = sqrt(y);
            result.push_back(root);
            result.push_back(-root);
        }
    } else if (D > 0.0) {
        double sqD = sqrt(D);
        double y1 = (-b + sqD) / (2.0 * a);
        double y2 = (-b - sqD) / (2.0 * a);
        
        if (abs(y1) < eps) {
            result.push_back(0.0);
        } else if (y1 > 0.0) {
            double root1 = sqrt(y1);
            result.push_back(root1);
            result.push_back(-root1);
        }
        
        if (abs(y2) < eps) {
            bool zero_exists = false;
            for (double root : result) {
                if (abs(root) < eps) {
                    zero_exists = true;
                    break;
                }
            }
            if (!zero_exists) {
                result.push_back(0.0);
            }
        } else if (y2 > 0.0) {
            double root2 = sqrt(y2);
            result.push_back(root2);
            result.push_back(-root2);
        }
    }
    
    return result;
}

int main(int argc, char* argv[]) {
    double a, b, c;
    
    a = get_coef(1, "Введите коэффициент A: ", argc, argv);
    b = get_coef(2, "Введите коэффициент B: ", argc, argv);
    c = get_coef(3, "Введите коэффициент C: ", argc, argv);
    
    vector<double> roots = get_roots(a, b, c);
    
    sort(roots.begin(), roots.end());
    
    int len_roots = roots.size();
    if (len_roots == 0) {
        cout << "Нет действительных корней" << endl;
    } else if (len_roots == 1) {
        cout << "Один корень: " << roots[0] << endl;
    } else if (len_roots == 2) {
        cout << "Два корня: " << roots[0] << " и " << roots[1] << endl;
    } else if (len_roots == 3) {
        cout << "Три корня: " << roots[0] << ", " << roots[1] 
             << " и " << roots[2] << endl;
    } else if (len_roots == 4) {
        cout << "Четыре корня: " << roots[0] << ", " << roots[1] 
             << ", " << roots[2] << " и " << roots[3] << endl;
    }
    
    return 0;
}