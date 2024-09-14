#include <stdio.h>
#include <stdlib.h>
int main() {
	FILE *input;
	FILE *output;
	char string[100];
	input = fopen("input.txt", "r");
	output = fopen("output.txt", "w");
	fgets(string, 100, input);
	fprintf(output, "%s", string);
	fclose(input);
	fclose(output);
	return 0;
}