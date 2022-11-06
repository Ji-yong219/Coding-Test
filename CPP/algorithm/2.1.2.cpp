#include <stdio.h>

int main(void){
    int i = 0;
    int j = 0;
    int user_count = 0;

    printf("input : ");
    scanf("%d", &user_count);

    for(i = 1 ; i <= user_count ; i++){
        for(j = user_count - i ; j > 0 ; j--){
            printf(" ");
        }
        
        for(j = 0 ; j < i ; j++){
            printf("*");
        }

        printf("\n");
    }

    return 0;
}