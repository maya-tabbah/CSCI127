// Maya Tabbah 
// maya.tabbah40@myhunter.cuny.edu 
// April 20, 2022 
// A while loop using C++ 


#include <iostream> 
using namespace std; 

int year; 

int main()
{
    cout << "Enter year ";
    cin >> year; 

    while (year > 2018)
    {
        cout << "Enter year ";
        cin >> year; 
    }

    cout << "You entered " << year; 

    return 0; 
}