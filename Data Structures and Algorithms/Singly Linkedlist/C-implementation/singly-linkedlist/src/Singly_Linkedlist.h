/*
    Singly Linkedlist (Implementation in C)
    - Singly_Linkedlist.h
    - Main.c
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
    int data;
    struct Node* next;
};

struct Singly_Linkedlist {
    struct Node* head;
    int number_of_elements;
    int memory_usage;
};

// TODO: Need to implement this function.
struct Singly_Linkedlist* create_linkedlist();

// TODO: Need to implement this function.
bool is_empty(struct Singly_Linkedlist* linkedlist);

// TODO: Need to implement this function.
void print_linkedlist(struct Singly_Linkedlist* linkedlist);

// TODO: Need to implement this function.
void get_linkedlist_stats(struct Singly_Linkedlist* linkedlist);

// TODO: Need to implement this function.
struct Singly_Linkedlist* insert_head(struct Singly_Linkedlist* linkedlist, int data);

// TODO: Need to implement this function.
struct Singly_Linkedlist* remove_head(struct Singly_Linkedlist* linkedlist);

// TODO: Need to implement this function.
struct Singly_Linkedlist* insert_tail(struct Singly_Linkedlist* linkedlist, int data);

// Need to implement this function.
struct Singly_Linkedlist* remove_tail(struct Singly_Linkedlist* linkedlist);