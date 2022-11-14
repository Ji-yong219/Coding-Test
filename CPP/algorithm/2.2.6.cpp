#include <iostream>

using namespace std;

int main(void) {
    int count_of_player = 0;
    int i = 0;
    int j = 0;
    int max_dice = 0;
    int max_reward = 0;
    int dice[3] = {0, };
    int result = 0;

    cin >> count_of_player;

    for (i = 0; i < count_of_player; i++) {
        for (j = 0; j < 3; j++) {
            cin >> dice[j];
            if (dice[j] > max_dice) {
                max_dice = dice[j];
            }
        }

        if (dice[0] == dice[1] && dice[1] == dice[2]) {
            result = 10000 + dice[0] * 1000;
        } else if (dice[0] == dice[1]) {
            result = 1000 + dice[0] * 1000;
        } else if (dice[1] == dice[2]) {
            result = 1000 + dice[1] * 1000;
        } else if (dice[0] == dice[2]) {
            result = 1000 + dice[0] * 1000;
        } else {
            result = max_dice * 100;
        }
        if (result > max_reward) {
            max_reward = result;
        }
    }
    printf("%d", max_reward);

    return 0;
}