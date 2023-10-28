#include <stdio.h>
#include <conio.h>

void main()
{
    int size = 10;
    int queue[size];
    int FRONT = 0, REAR = -1;
    void enqueue(int a)
    {
        if (REAR == size - 1)
        {
            printf("Overflow\n");
        }
        else
        {
            REAR = REAR + 1;
            queue[REAR] = a;
        }
    };
    void dequeue()
    {
        if (FRONT == -1)
        {
            printf("Underflow\n");
        }
        else
        {
            printf("-> %d\n", queue[FRONT]);
            FRONT = FRONT + 1;
        }
    };
    void display()
    {
        for (int i = FRONT; i <= REAR; i++)
        {
            printf("%d, ", queue[i]);
        }
        printf("\n");
    }
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);
    enqueue(6);
    enqueue(7);
    enqueue(8);
    enqueue(9);
    enqueue(10);
    display();
    enqueue(11);
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    display();
};