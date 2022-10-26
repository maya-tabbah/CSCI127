// Maya Tabbah 
// maya.tabbah40@myhunter.cuny.edu
// April 20, 2022
// This C++ program returns a greeting based on a user input of the season

#include <iostream> 
using namespace std; 

int main()
{
    int numMonth;
    cout << "Enter the month(as a number)";
    cin >> numMonth; 

    if (numMonth < 3 or numMonth > 11)
    {
        cout << "Happy Winter";
    }

    else if (numMonth >= 3 and numMonth <= 6)
    {
        cout << "Happy Spring";
    }

    else if (numMonth == 7 or numMonth == 8)
    {
        cout << "Happy Summer";
    } 

    else
    {
        cout << "Happy Fall";
    }

    return 0; 
}