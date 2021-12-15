#include <iostream>
#include <vector>
using namespace std;
void printfactors(vector<int> all, int x)
{
    cout << "The prime factors of " << x << " are: ";
    int prev = all[0];
    int count = 0;
    for (int i = 0; i < all.size(); i++)
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
vector<int> findprime(int x)
{
    for (int i = 2; i < x; i++)
    {
        if ((x % i == 0))
        {
            int y = x / i;
            vector<int> a, b, c;
            a = findprime(i);
            b = findprime(y);
            c.resize(b.size() + a.size());
            merge(a.begin(), a.end(), b.begin(), b.end(), c.begin());
            sort(c.begin(), c.end());
            return c;
        }
    }
    vector<int> a;
    a.resize(1);
    a[0] = x;
    return a;
}
int main()
{
    int number;
    cout << "Enter a number you want to find the prime factors of: ";
    cin >> number;
    printfactors(findprime(number), number);
    return 0;
}