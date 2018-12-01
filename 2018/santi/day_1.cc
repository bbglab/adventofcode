#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(){
	int current;
	vector<int> op;
	while (cin >> current){
		op.push_back(current);
	}

	int res = 0;
	map<int, int> vist;
	vist[res] = 1;

	while (1==1){
		for (int i =0; i< op.size(); i++){
			res = res + op[i];
			if(vist[res] == 1){
				cout << res << endl;
				return(1);
			}
			vist[res] = 1;
		}
	}
}
