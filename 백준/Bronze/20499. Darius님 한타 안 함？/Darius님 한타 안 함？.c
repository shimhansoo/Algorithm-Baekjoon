int main()
{
    int kill;
    int assist;
    int death;
    char slash;
    
    scanf("%d%c%d%c%d",&kill,&slash,&death,&slash,&assist);
    if( kill + assist < death || death == 0)
    {
        printf("hasu");
    }
    else
    {
        printf("gosu");
    }
}