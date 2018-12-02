#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main(){
	string current;
	int two;
	int three;
	bool btwo;
	bool bthree;
	vector<int> count;
	while (cin >> current){
		count = vector<int>(255,0);
		for(int i = 0; i < current.size(); i++){
			count[current[i]]++;
		}
		btwo = bthree = false;
		for(int i = 0; i < 250; i++){
			btwo = (count[i] == 2) or btwo;
			bthree = (count[i] == 3) or bthree;
		}
		if(btwo) two++;
		if(bthree) three++;
	}
	cout << two * three << endl;
}

