#include <iostream>

using namespace std;

int main(void) {
    int i = 0;
    int count_of_problem = 0;
    int grading_arr_of_problem[100] = {0, };
    int grading_of_problem;
    int correct_acc_count = 0;
    int result = 0;

    scanf("%d", &count_of_problem);

    for (i = 0; i < count_of_problem; i++) {
        cin >> grading_of_problem;

        if (grading_of_problem == 0) {
            correct_acc_count = 0;
        } else if (grading_of_problem == 1) {
            result += grading_of_problem + correct_acc_count;
            correct_acc_count++;
        }
    }
    printf("%d", result);

    return 0;
}