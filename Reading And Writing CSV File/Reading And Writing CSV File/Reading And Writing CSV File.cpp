#include <iostream>
#include<fstream>
using namespace std;
void read()
{
	ifstream fin;
	string line;
	// Open an existing file
	fin.open("H:/sir zeeshan work/test/0/39907_ortho_1-1_1n_s_il001_2017_1.csv");
	while (!fin.eof()) {
		fin >> line;
		cout << line << " ";
	}
}
int main()
{
	read();
	return 0;
}