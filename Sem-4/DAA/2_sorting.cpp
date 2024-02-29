#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// ! QUICK SORT
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void display(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " | ";
    }
    cout << endl;
}

int counter = 0;
int quick_partition(int arr[], int low, int high)
{
    counter++;
    // int mid = low + (high - low) / 2;
    int pivot = arr[low];
    // cout << "Pivot: " << pivot << endl;
    // display(arr, high);
    int i = low;
    int j = high;

    // do
    // {
    //     i++;
    // } while (arr[i] < pivot);

    // while (i < j)
    // {
    //     do
    //     {
    //         j--;
    //     } while (arr[j] > pivot);

    //     if (i < j)
    //     {
    //         swap(arr[i], arr[j]);
    //     }
    // }

    do
    {
        do
        {
            i++;
        } while (arr[i] < pivot);

        do
        {
            j--;
        } while (arr[j] > pivot);

        if (i < j)
        {
            swap(arr[i], arr[j]);
            // display(arr, high);
        }
    } while (i < j);

    swap(arr[low], arr[j]);
    // display(arr, high);
    // cout << "--------------------" << endl;

    return j;
}

int qSort(int arr[], int low, int high)
{
    int j;
    if (low < high)
    {
        j = quick_partition(arr, low, high);
        qSort(arr, low, j - 1);
        qSort(arr, j + 1, high);
    }
}

// ! MERGE SORT
void merge(int A[], int B[], int n, int m)
{
    int i = 0, j = 0, k = 0;
    while (i < n && j < m)
    {
        if (A[i] < B[j])
        {
            A[k++] = A[i++];
        }
        else
        {
            A[k++] = B[j++];
        }
    }
    while (i < n)
    {
        A[k++] = A[i++];
    }
    while (j < m)
    {
        A[k++] = B[j++];
    }
}

void mergeSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        // merge(arr, low, mid, high);
    }
}

int main()
{
    int s = 10;
    int arr[s] = {};
    for (int i = 0; i < s; i++)
    {
        arr[i] = rand() % 100;
    }
    int len = sizeof(arr) / sizeof(arr[0]);
    display(arr, len);
    qSort(arr, 0, len - 1);
    display(arr, len);

    // for (int i = 0; i < len; i++)
    // {
    //     cout << arr[i] << " ";
    // }
    // cout << endl;
    return 0;
}