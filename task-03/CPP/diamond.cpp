#include <iostream>
#include <string>
using namespace std;
int main () {
	int num;
	cin >> num;
	string star(num, ' ');
	for (int i = 0; i < num; i++) {
		star = star.substr(1);
		star += " *";
		cout << star << "\n";
	}
	for (int j = 0; j < num; j++) {
		star = star.substr(0, star.length() - 2);
		star = " " + star;
		cout << star << "\n";
	}
	return 0;
}