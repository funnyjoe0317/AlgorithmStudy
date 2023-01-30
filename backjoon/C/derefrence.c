#include <stdio.h>

int main(){
    int a = 10, b = 20, temp;
    int *x,*y;
    x = &a;
    y = &b;
    printf("a: %d b: %d\n", a,b);
    temp = *x;
    *x= *y;
    *y =temp;
    printf("a : %d b: %d\n", a,b);

    return 0;
    
}