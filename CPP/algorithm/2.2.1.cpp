#include <iostream>

using namespace std;

int main(void) {
    int i = 0;
    int user_count = 0;
    int user_numbers[1000] = {-10000, };

    scanf("%d", &user_count);

    for (i = 0; i < user_count; i++) {
        cin >> user_numbers[i];
    }

    for (i = user_count - 1; i >= 0; i--) {
        printf("%d ", user_numbers[i]);
    }

    return 0;
}