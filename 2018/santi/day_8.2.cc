#include <iostream>
#include <vector>
using namespace std;

int read_node(){
	int childs;
	int metadata;
	int result = 0;
	vector<int> values;
	cin >> childs >> metadata;
	for (int i = 0; i < childs; i++){
		values.push_back(read_node());
	}
	if(childs == 0){
		for(int i = 0; i < metadata; i++){
			cin >> childs;
			result = result + childs;
		}
	}
	else{
		for(int i = 0; i < metadata; i++){
			cin >> childs;
			if(values.size() > childs -1){
				result = result + values[childs -1];
			}
		}
	}
	return result;
}

int main(){
	cout << read_node() << endl;
}


