
int main()
{
    int S,K,H;
    int min,max;
    scanf("%d %d %d", &S, &K, &H);
    
    int sum = S + K + H;
    if(sum >= 100)
    {
        printf("OK");
    }
    else if(sum < 100)
    {
        if(S > K)
        {
            max = S;
            min = K;
        }
        else
        {
            max = K;
            min = S;
        }
        if(H > max)
        {
            max = H;
        }
        if(H < min)
        {
            min = H;
        }
        if(min == S)
        {
            printf("Soongsil");
        }
        else if(min == K)
        {
            printf("Korea");
        }
        else if(min == H)
        {
            printf("Hanyang");
        }
    }
}