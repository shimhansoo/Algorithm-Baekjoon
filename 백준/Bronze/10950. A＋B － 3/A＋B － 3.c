#include<stdio.h>

int main()

{
    int x;
    scanf("%d", &x);
    int a,b;
    

    for(int i = 0; i < x; i++)
    {
        scanf("%d%d",&a,&b);
        printf("%d\n", a + b);
    }
}