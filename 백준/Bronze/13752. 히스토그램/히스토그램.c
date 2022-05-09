int main()
{
    int test;
    int num;
    scanf("%d", &test);
    
    for(int i = 0; i < test; i++)
    {
        scanf("%d", &num);
        for(int j = 0; j < num; j++)
        {
            printf("=");
        }
        printf("\n");
    }
}