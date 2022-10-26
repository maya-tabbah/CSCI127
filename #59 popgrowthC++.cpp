// Maya Tabbah 
// maya.tabbah40@myhunter.cuny.edu 
// April 20, 2022 
// This program prints the population based on user entry. 

#include <iostream> 
#include <iomanip> 
using namespace std; 

int yearsINP;
int years;
float population;
float b;
float d;  


int main()
{
    cout << "Enter the number of years: "; 
    cin >> yearsINP; 
    
    float population = 325.70;
    float b = 12.4/1000;
    float d = 8.4/1000;
    
    
    for (years = 2017; years <= yearsINP+2017; years++)
    {
        cout << setprecision(2) << fixed;
        cout << "Year " << years << "\t" << population << "\n"; 
        population = population + (b*population) - (d*population);
    }
    return 0;
}