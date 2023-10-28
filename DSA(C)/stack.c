#include <stdio.h>
#include <conio.h>
#define size 10

void main()
{
    int stack[size];
    int pointer = -1;
    int *TOP = &pointer;
    void push(int stack[], int a, int *TOP);
    void pop(int stack[], int *TOP);
    void display(int stack[], int *TOP);
    push(stack, 10, TOP);
    push(stack, 20, TOP);
    push(stack, 30, TOP);
    display(stack, TOP);
    pop(stack, TOP);
    display(stack, TOP);
}
void push(int stack[], int a, int *TOP)
{
    if (*TOP == size - 1)
    {
        printf("Overflow\n");
    }
    else
    {
        *TOP = *TOP + 1;
        stack[*TOP] = a;
    }
}
void pop(int stack[], int *TOP)
{
    if (*TOP == -1)
    {
        printf("Underflow\n");
    }
    else
    {
        printf("-> %d\n", stack[*TOP]);
        *TOP = *TOP - 1;
    }
}
void display(int stack[], int *TOP)
{
    for (int i = *TOP; i >= 0; i--)
    {
        printf("%d |", stack[i]);
    }
}