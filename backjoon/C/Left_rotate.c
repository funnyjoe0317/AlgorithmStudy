#include <stdio.h>

void leftrotate(struct node* temp)
{
    struct node* right = temp -> r;
    temp -> r = right -> l;
    if (temp -> r)
        temp -> r ->p = x ;
    right -> 
}