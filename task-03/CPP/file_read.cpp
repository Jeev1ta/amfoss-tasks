#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main () {
	ifstream input("input.txt");
	ofstream output("output.txt");
	output << input.rdbuf();
	input.close();
	output.close();
	return 0;
}