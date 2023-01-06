#include<iostream>
using namespace std; 

int findCeiling(int arr[], int target, int n){
    int start = 0; 
    int end = n-1; 
    while (start<=end)
    {
        int mid = start + (end-start)/2; 
        if (arr[mid]==target)
        {
            return mid; 
        }
        else if (arr[mid]>target)
        {
            end = mid-1; 
        }
        else{
            start = mid+1; 
        }
        
    }
    return arr[start]; 
    
    
}
int main(){
    int n; 
    cin>>n; 
    int arr[n]; 
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i]; 
    }
    

    //ceiling = the smallest number which is greater or equal to target. do this question with binary search 
    int target;
    cin>>target;
    cout<<findCeiling(arr, target, n);
   
   
    
    
}