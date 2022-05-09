#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    
    for(int i = 0; i < a; i++)
    {
        printf("Hello World, Judge %d!\n",i + 1);
    }
    
    return 0;
}