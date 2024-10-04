/*
    Singly Linkedlist (Implementation in C)
    - Singly_Linkedlist.c
    - Singly_Linkedlist.h
    - Main.c
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include "Singly_Linkedlist.h"

struct Singly_Linkedlist* create_linkedlist() {
    printf("\nfunction create_linkedlist() called -->\n");

    sleep(1);
    printf("\tcreating new head node for linkedlist.\n");
    struct Node* head = (struct Node*) malloc(sizeof(struct Node));
    if (!head) {
        sleep(2);
        printf("Memory error\n");
        return NULL;
    }
    head -> data = 0;
    head -> next = NULL;

    sleep(1);
    printf("\tcreating linkedlist structure.\n");
    struct Singly_Linkedlist* linkedlist = (struct Singly_Linkedlist*) malloc(sizeof(struct Singly_Linkedlist));
    if (!linkedlist) {
        sleep(2);
        printf("Memory error\n");
        free(head);
        return NULL;
    }

    linkedlist -> head = head;
    linkedlist -> number_of_elements = 0;
    linkedlist -> memory_usage = linkedlist -> number_of_elements * sizeof(struct Node);

    sleep(1);
    printf("linkedlist successfully created.\n");

    return linkedlist;
}