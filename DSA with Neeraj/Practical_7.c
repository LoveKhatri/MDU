/*
Program to implement Linked List
Author: Neeraj
Date: October 30, 2023
*/

#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *start = NULL;

void insert_at_beginning(int);
void insert_at_end(int);
void insert_at_position(int, int);
void delete_from_beginning();
void delete_from_end();
void delete_from_position(int);
void display();

int main()
{
    int choice, item, position;
    while(1)
    {
        printf("\n\n1. Insert at beginning\n2. Insert at end\n3. Insert at position\n4. Delete from beginning\n5. Delete from end\n6. Delete from position\n7. Display\n8. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1:
                printf("\nEnter the element to be inserted: ");
                scanf("%d", &item);
                insert_at_beginning(item);
                break;
            case 2:
                printf("\nEnter the element to be inserted: ");
                scanf("%d", &item);
                insert_at_end(item);
                break;
            case 3:
                printf("\nEnter the element to be inserted: ");
                scanf("%d", &item);
                printf("\nEnter the position: ");
                scanf("%d", &position);
                insert_at_position(item, position);
                break;
            case 4:
                delete_from_beginning();
                break;
            case 5:
                delete_from_end();
                break;
            case 6:
                printf("\nEnter the position: ");
                scanf("%d", &position);
                delete_from_position(position);
                break;
            case 7:
                display();
                break;
            case 8:
                exit(0);
            default:
                printf("\nInvalid choice");
        }
    }
    return 0;
}

void insert_at_beginning(int item)
{
    struct node *new_node;
    new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = item;
    new_node->next = start;
    start = new_node;
}

void insert_at_end(int item)
{
    struct node *new_node, *ptr;
    new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = item;
    new_node->next = NULL;
    if(start == NULL)
        start = new_node;
    else
    {
        ptr = start;
        while(ptr->next != NULL)
            ptr = ptr->next;
        ptr->next = new_node;
    }
}

void insert_at_position(int item, int position)
{
    struct node *new_node, *ptr;
    int i;
    new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = item;
    if(position == 1)
    {
        new_node->next = start;
        start = new_node;
    }
    else
    {
        ptr = start;
        for(i = 1; i < position - 1; i++)
        {
            if(ptr == NULL)
            {
                printf("\nPosition out of range");
                return;
            }
            ptr = ptr->next;
        }
        new_node->next = ptr->next;
        ptr->next = new_node;
    }
}

void delete_from_beginning()
{
    struct node *ptr;
    if(start == NULL)
        printf("\nList is empty");
    else
    {
        ptr = start;
        start = start->next;
        free(ptr);
    }
}

void delete_from_end()
{
    struct node *ptr, *preptr;
    if(start == NULL)
        printf("\nList is empty");
    else if(start->next == NULL)
    {
        ptr = start;
        start = NULL;
        free(ptr);
    }
    else
    {
        ptr = start;
        while(ptr->next != NULL)
        {
            preptr = ptr;
            ptr = ptr->next;
        }
        preptr->next = NULL;
        free(ptr);
    }
}

void delete_from_position(int position)
{
    struct node *ptr, *preptr;
    int i;
    if(start == NULL)
        printf("\nList is empty");
    else if(position == 1)
    {
        ptr = start;
        start = start->next;
        free(ptr);
    }
    else
    {
        ptr = start;
        for(i = 1; i < position; i++)
        {
            if(ptr == NULL)
            {
                printf("\nPosition out of range");
                return;
            }
            preptr = ptr;
            ptr = ptr->next;
        }
        preptr->next = ptr->next;
        free(ptr);
    }
}

void display()
{
    struct node *ptr;
    if(start == NULL)
        printf("\nList is empty");
    else
    {
        ptr = start;
        while(ptr != NULL)
        {
            printf("%d\t", ptr->data);
            ptr = ptr->next;
        }
    }
}