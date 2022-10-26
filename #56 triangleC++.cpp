//Maya Tabbah 
//maya.tabbah40@myhunter.cuny.edu 
//April 19, 2022 
//C++ programs that draws a triangle the height the user inputs 


#include <iostream> 
using namespace std; 

int num; 
int i;
int j;

int main()
{
    int num;
    cout << "Enter a number: "; 
    cin >> num; 

    for (i = 0; i <= num; i++){
        for(j = 0; j <= i; j++){
            cout << "*" ;

        }
        cout << "\n";
    }

    return 0;


}