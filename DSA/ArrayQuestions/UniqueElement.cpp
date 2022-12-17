#include <iostream>
using namespace std;

int findUnique(int arr[], int n)
{
    int ans = 0;
    //using xor gate to find unique element. 
    // a^a =0; 
    // xor of similar element is always zero 
    
    for (int i = 0; i < n; i++)
    {
        ans = ans ^ arr[i];
    }

    return ans;
}

int main()
{

    int c;
    cin >> c;
    while (c > 0)
    {
        int n;
        int m;
        cin >> m;

        n = 2 * m + 1;
        int arr[n];

        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        int unique = findUnique(arr, n);

        cout << unique;

        c--;
    }

    return 0;
}