#include <iostream>
#include <map>
#include <vector>
using namespace std;

bool react(char a, char b){
	if(a - 'a'  < 0){
		return ((a - 'A' + 'a' - b) == 0);
	}
	if(b - 'a' < 0){
		return ((b - 'A' + 'a' - a) == 0);
	}
	return false;
}

int main(){
	string poli;
	cin >> poli;
	int i = 0;
	while(i < poli.size() - 1){
		if(react(poli[i], poli[i+1])){
			poli.erase(i,2);
			i--;
			if(i < 0) i = 0;
		}
		else{
			i++;
		}
	}
	cout << poli.size() << endl;
}


