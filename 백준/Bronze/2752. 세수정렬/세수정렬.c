#include <stdio.h>

int main()
{
    int arr[3];
    int min = 1000001;
    int mid = 0;
    int max = 0;

    for(int i = 0; i < 3; i++)
    {
        scanf("%d", &arr[i]);
        if(arr[i] > max)
            max = arr[i];
        if(arr[i] < min)
            min = arr[i];
    }
    for(int k = 0; k < 3; k++)
    {
        if(arr[k] > min)
        {
            if(arr[k] < max)
            {
                mid = arr[k];
            }
        }
    }

    arr[0] = min;
    arr[1] = mid;
    arr[2] = max;

    for(int j = 0; j < 3; j++)
    {
        printf("%d ",arr[j]);
    }

    return 0;
}