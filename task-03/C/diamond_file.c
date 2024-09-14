#include <stdio.h>
#include <stdlib.h>
int main() {
	FILE *input;
	FILE *output;
	int num;
	input = fopen("input.txt", "r");
	output = fopen("output.txt", "w");
	fscanf(input, "%d", &num);
    for(int i = 1; i <= num; i++) {
        for(int j = 0; j < num-i; j++) {
            fprintf(output, "%s", " ");
        }
        for(int k = 0; k < i; k++) {
            fprintf(output,"%s", "* ");
        }
        fprintf(output, "%s", "\n");
    }
    for(int i = num-1; i >= 1; i--) {
        for(int j = num-i-1; j >= 0; j--) {
            fprintf(output,"%s", " ");
        }
        for(int k = 0; k < i; k++) {
            fprintf(output,"%s", "* ");
        }
        fprintf(output,"%s", "\n");
    }
	fclose(input);
	fclose(output);
	return 0;
}