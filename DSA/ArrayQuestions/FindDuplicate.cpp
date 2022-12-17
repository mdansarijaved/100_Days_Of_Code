// Write a program to find the duplicate element in an array of size N+1. The array contains elements from 1 to N. The array is sorted. The array contains one duplicate element.
//  Input Format
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        ans = ans ^ arr[i];
    }

    for (int i = 1; i <= n - 1; i++)
    {
        ans = ans ^ i;
    }

    cout << ans;
}