#include <iostream>
#include <math.h>
#include <complex>
using namespace std;

void quadratic(long double a, long double b, long double c)
{
    complex<long double> x, y;
    x = ((-b + sqrt(complex<long double>((b * b) - (4 * a * c)))) / (2 * a));
    y = ((-b - sqrt(complex<long double>((b * b) - (4 * a * c)))) / (2 * a));
    if (x == y)
    {
        cout << "The only answer is: " << x << endl;
    }
    string newx;
    string newy;
    if (x.imag() != 0)
    {
        newx = to_string(x.imag()) + "i" + " + " + to_string(x.real());
    }
    else
    {
        newx = to_string(x.real());
    }
    if (y.imag() != 0)
    {
        newy = to_string(y.imag()) + "i" + " + " + to_string(y.real());
    }
    else
    {
        newy = to_string(y.real());
    }
    cout << "The first answer is: " << newx << "\nThe second answer is: " << newy << endl;
}

int main()
{
    long double a, b, c;
    cout << "Enter the a, b, and c of ax^2 + bx + c: " << endl;
    cin >> a >> b >> c;
    quadratic(a, b, c);
    return 0;
}