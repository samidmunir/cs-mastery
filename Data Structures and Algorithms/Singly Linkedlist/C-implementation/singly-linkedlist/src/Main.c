/*
    Singly Linkedlist (C implementation)
    - Main.c
*/

#include <stdio.h>
#include <stdlib.h>
#include "Singly_Linkedlist.h"

int main(int argc, char* argv[]) {
    printf("Singly Linked List (C Implementation)\n");

    struct Singly_Linkedlist* linkedlist = create_linkedlist();

    return EXIT_SUCCESS;
}