#include <stdio.h>
int main(void){
    int nCount = 0;
    int i = 0;
    int j = 0;

    printf("Enter Number : ");
    scanf("%d", &nCount);

    for(i = 0 ; i < nCount ; i++){
        for(j = 0 ; j < i+1 ; j++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}