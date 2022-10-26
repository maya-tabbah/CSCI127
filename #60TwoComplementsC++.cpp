// Maya Tabbah 
// maya.tabbah40@myhunter.cuny.edu 
// April 24, 2022
// this program prints out the number (between -31-31) 
//the user entered in the two complements form

#include <iostream> 
using namespace std; 

int n;
int x; 
int b;
int main(){
    cout << "Enter a whole number beteen -31 and 31: ";
    cin >> n; 

    if (n < 0){
        cout << "1"; 
        x = 32 + n; 
    }

    else if (n >= 0){
        cout << "0";
        x = n;
    }

    int b = 16;
    while(b > 0.5){
        if(x >= b){
            cout << "1";
        }
        else{
            cout << "0";
        }
        x = x%b;
        b = b/2; 
    }
    cout << "\n";
}