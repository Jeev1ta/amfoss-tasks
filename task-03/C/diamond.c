#include <stdio.h>
int main() {
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++) {
        for(int j = 0; j < num-i; j++) {
            printf(" ");
        }
        for(int k = 0; k < i; k++) {
            printf("* ");
        }
        printf("\n");
    }
    for(int i = num-1; i >= 1; i--) {
        for(int j = num-i-1; j >= 0; j--) {
            printf(" ");
        }
        for(int k = i - 1; k >= 0; k--) {
            printf("* ");
        }
        printf("\n");
    }
}