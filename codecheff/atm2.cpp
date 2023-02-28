#include <iostream> 
using namespace std; 
int main(){
    int t = 0; 
    while (t > 0){
        int x ,y; 
        cin>>x>>y; 
        int withdraw[x]; 
        for(int i = 0; i < x; i++){
            cin>>withdraw[i]; 
        }
        for(int i = 0 ; i < x ; i++){
            cout<<withdraw[i]<<endl;
        }
    }
}