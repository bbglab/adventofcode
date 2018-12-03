#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(){
	int id, x, y, w, h;
	int overlap = 0;
	char symbol;
	short int fabric[1000][1000] = {0};
	while (cin >> symbol){
		if(symbol == '#'){
			cin >> id >> symbol >> x >> symbol >> y >> symbol >> w  >> symbol >> h;
		}
		else{
			cerr << "Bad read" << endl;
		}

		for (int i = x; i < x+w; i++){
			for(int j = y; j < y+h ; j++){
				if(fabric[i][j] == 1) overlap++;
				fabric[i][j]++;
			}
		}
	}
	cout << overlap << endl;
}


