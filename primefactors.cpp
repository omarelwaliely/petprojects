#include <iostream>
#include <vector>
using namespace std;

void printfactors(vector<long long> all, long long x)
{
    sort(all.begin(), all.end());
    cout << "The prime factors of " << x << " are: ";
    long long prev = all[0];
    long long count = 0;
    for (long long i = 0; i < all.size(); i++)
    {
        if (all[i] == prev)
        {
            count++;
        }
        else
        {
            cout << prev << "^" << count << " * ";
            count = 1;
        }
        prev = all[i];
    }
    cout << prev << "^" << count << endl;
}
vector<long long> findprime(long long x)
{
    for (long long i = 2; i <= sqrt(x); i++)
    {
        if ((x % i == 0))
        {
            long long y = x / i;
            vector<long long> a, b, c;
            a = findprime(i);
            b = findprime(y);
            c.resize(b.size() + a.size());
            merge(a.begin(), a.end(), b.begin(), b.end(), c.begin());
            return c;
        }
    }
    vector<long long> a;
    a.resize(1);
    a[0] = x;
    return a;
}
int main()
{
    long long number;
    cout << "Enter a number you want to find the prime factors of (if x<1, |x| will be computed): ";
    cin >> number;
    if (number < 0)
    {
        number *= -1;
    }
    printfactors(findprime(number), number);
    return 0;
}
