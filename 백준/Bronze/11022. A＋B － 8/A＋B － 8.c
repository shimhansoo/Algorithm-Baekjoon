#include<stdio.h>

int main()

{
    int x;
    scanf("%d", &x);
    int a,b;
    

    for(int i = 0; i < x; i++)
    {
        scanf("%d%d",&a,&b);
        printf("Case #%d: %d + %d = %d\n",i + 1,a,b, a + b);
    }
}