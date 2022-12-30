#include<iostream>
using namespace std; 

int main(){
    int n; 
    cin>>n; 
    int arr[n]; 
    for(int i=0; i<n; i++){
        cin>>arr[i]; 
    }   
    int target; 
    cin>>target; 
    int i=0; 
    int j=n-1;
    while(i<j){
        int sum = arr[i] + arr[j]; 
        if(sum == target){
            cout<<i<<" and "<<j<<endl; 
            i++; 
            j--; 
        }
        else if(sum > target){
            j--; 
        }
        else{
            i++; 
        }
    }
}