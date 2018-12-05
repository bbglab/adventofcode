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
	string poli_save = poli;
	int i;
	int res = poli.size();
	for(int j = 0; j < ('z' - 'a' + 1); j++){
		poli = poli_save;
		i = 0; 
		while(i < poli.size() - 1){
			if(poli[i] == 'a' + j or poli[i] == 'A' + j){
				poli.erase(i,1);
				i--;
				if(i < 0) i = 0;
			}
			if(react(poli[i], poli[i+1])){
				poli.erase(i,2);
				i--;
				if(i < 0) i = 0;
			}
			else{
				i++;
			}
		}
		if(res > poli.size()) res = poli.size();
	}
	cout << res << endl;
}


