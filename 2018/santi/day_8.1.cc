#include <iostream>
#include <vector>
using namespace std;

int read_node(){
	int childs;
	int metadata;
	int result = 0;
	cin >> childs >> metadata;
	for (int i = 0; i < childs; i++){
		result = result + read_node();
	}
	for(int i = 0; i < metadata; i++){
		cin >> childs;
		result = result + childs;
	}
	return result;
}

int main(){
	cout << read_node() << endl;
}


