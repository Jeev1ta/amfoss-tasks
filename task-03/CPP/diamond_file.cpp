#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main () {
	ifstream input("input.txt");
	ofstream output("output.txt");
	int num;
	input >> num;
	string star(num, ' ');
	for (int i = 0; i < num; i++) {
		star = star.substr(1);
		star += " *";
		output << star << "\n";
	}
	for (int j = 0; j < num; j++) {
		star = star.substr(0, star.length() - 2);
		star = " " + star;
		output << star << "\n";
	}
	input.close();
	output.close();
	return 0;
}