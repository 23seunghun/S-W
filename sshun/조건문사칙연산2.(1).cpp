#include <stdio.h>
//202395020 신승훈
//2023 10 16  
int main(void)
{
    int opt;
    double num1, num2;
    double result;

    printf("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 \n");
    printf("선택?");
    scanf("%d", &opt);
    
    if (opt < 1 || opt > 4) {
        printf("잘못된 선택입니다, 다시 입력해 주세요.\n");
        return 0;
    }

    printf("첫 번째 정수 입력:");
    scanf("%lf", &num1);
    printf("두 번째 정수 입력:");
    scanf("%lf", &num2);

    if (opt == 1)
        result = num1 + num2;
    else if (opt == 2)
        result = num1 - num2;
    else if (opt == 3)
        result = num1 * num2;
    else
        result = num1 / num2;

    printf("결과: %g \n", result);
    return 0;
}

