#include <iostream>
using namespace std;

int main()
{
    cout << "Single catch block:";
    cout << "\nEnter 2 values: ";
    int a, b;
    cin >> a >> b;
    try
    {
        if (b == 0)
        {
            throw b;
        }
        else
        {
            cout << "\nNo Exception occured!\n";
            cout << a / b;
        }
    }
    catch (int a)
    {
        cout << "\nCannot divide by 0";
    }

    cout << "\n\nMultiple Catch Blocks";
    int x;
    double y;
    char z;
    cout << "\nEnter an integer: ";
    cin >> x;
    cout << "\nEnter a floating point number: ";
    cin >> y;
    cout << "\nEnter a character: ";
    cin >> z;
    try
    {
        if (x == 0)
        {
            throw x;
        }
        else if (y == 0.0)
        {
            throw y;
        }
        else if (z == a)
        {
            throw z;
        }
        else
        {
            cout << "\nNo Exception occured!\n";
            cout << a / b;
        }
    }
    catch (int a)
    {
        cout << "\nInteger cannot be 0";
    }
    catch (double a)
    {
        cout << "\nDouble cannot be 0";
    }
    catch (char a)
    {
        cout << "\nCharacter cannot be 0";
    }

    cout << "\nSingle catch block for all exceptions";
    cout << "\nEnter 2 values: ";
    
    cin >> a >> b;
    try
    {
        if (b == 0)
        {
            throw b;
        }
        else
        {
            cout << "\nNo Exception occured!\n";
            cout << a / b;
        }
    }
    catch (...)
    {
        cout << "\nCannot divide by 0";
    }
    return 0;
}