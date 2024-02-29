#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int iterativeBS(int arr[], int len, int target)
{
    int low = 0;
    int high = len - 1;

    int count = 0;
    while (low <= high)
    {
        count++;
        int mid = low + ((high - low) / 2);

        if (arr[mid] == target)
        {
            cout << "Count: " << count << endl;
            cout << "Our Complexity:" << log2(count) << endl;
            return mid;
        }
        if (target < arr[mid])
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    cout << "Count: " << count << endl;
    cout << "Our Complexity:" << log2(count) << endl;
    return -1;
};

int counter = 0;
int recursiveBS(int arr[], int low, int high, int target)
{
    counter++;
    if (low > high)
    {
        cout << "Count: " << counter << endl;
        cout << "Our Complexity:" << log2(counter) << endl;
        return -1;
    }

    int mid = low + ((high - low) / 2);
    if (arr[mid] == target)
    {
        cout << "Count: " << counter << endl;
        cout << "Our Complexity:" << log2(counter) << endl;
        return mid;
    }
    if (target < arr[mid])
    {
        return recursiveBS(arr, low, mid - 1, target);
    }
    else
    {
        return recursiveBS(arr, mid + 1, high, target);
    }
}

// ! This isn't required in the practical file, is here just for comparison
int linear_search(int arr[], int len, int target)
{
    int count = 0;
    for (int i = 0; i < len; i++)
    {
        count++;
        if (arr[i] == target)
        {
            cout << "Count: " << count << endl;
            cout << "Our Complexity:" << count << endl;
            return i;
        }
    }
    cout << "Count: " << count << endl;
    cout << "Our Complexity:" << count << endl;
    return -1;
}

int main()
{
    int A[1000] = {};
    for (int i = 0; i < 1000; i++)
    {
        A[i] = i * 2;
    }

    int target;
    cout << "Enter the number to search: ";
    cin >> target;

    int size = sizeof(A) / sizeof(A[0]);

    cout << "----Iterative Binary Search----" << endl;
    int iterative = iterativeBS(A, size, target);
    cout << "Original Complexity: " << log2(size) << endl;

    cout << "----Recursive Binary Search----" << endl;
    int recursive = recursiveBS(A, 0, size, target);
    cout << "Original Complexity: " << log2(size) << endl;

    cout << "----Linear Search----" << endl;
    int linear = linear_search(A, size, target);
    cout << "Original Complexity: " << size << endl;

    if (iterative != -1)
    {
        cout << "\n> Found at: " << iterative << endl;
    }
    else
    {
        cout << "\n> Not found" << endl;
    }
}
