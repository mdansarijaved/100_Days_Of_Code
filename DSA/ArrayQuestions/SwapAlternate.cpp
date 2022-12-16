#include <iostream>
using namespace std;

void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

void SwapArray(int arr[], int n)
{
    for (int i = 0; i < n; i += 2)
    {
        if (i + 1 < n)
        {

            
            //swap by using a third variable 
            int temp = 0 ; 
            temp = arr[i] ; 
            arr[i] = arr[i+1]; 
            arr[i+1]=temp; 

        }
    }
}

int main()
{
    int even[6] = {1, 3, 4, 5, 6, 7};
    int odd[7] = {2,3,5,5,6,5,6}; 

    SwapArray(even,6); 
    printArray(even,6); 

    cout<<endl; 

    SwapArray(odd,7); 
    printArray(odd,7); 
}