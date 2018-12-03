#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(){
	int id, x, y, w, h;
	map<int, bool> overlap;
	char symbol;
	short int fabric[1000][1000] = {0};
	while (cin >> symbol){
		if(symbol == '#'){
			cin >> id >> symbol >> x >> symbol >> y >> symbol >> w  >> symbol >> h;
		}
		else{
			cerr << "Bad read" << endl;
		}
		overlap[id] = true;
		for (int i = x; i < x+w; i++){
			for(int j = y; j < y+h ; j++){
				if(fabric[i][j] != 0){
					overlap[id] = false;
					overlap[fabric[i][j]] = false;
				}
				fabric[i][j] = id;
			}
		}
	}

	for(map<int,bool>::iterator i = overlap.begin(); i != overlap.end(); ++i){
		if(i->second) cout << i->first << endl;
	}
}


