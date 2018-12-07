#include <iostream>
#include <vector>
using namespace std;

int main(){
	int xpos;
	int ypos;
	char symbol;
	int maxx = 0;
	int maxy = 0;
	vector<int> x;
	vector<int> y;
	int distance;
	int count = 0;
	
	while(cin>> xpos >> symbol >> ypos){
		x.push_back(xpos);
		y.push_back(ypos);
		if(maxx < xpos)  maxx = xpos;
		if(maxy < ypos) maxy = ypos;
	}
	maxx = maxx + 2;
	maxy = maxy +2;
	vector<vector<int> > dmatrix = vector<vector<int> >(maxx, vector<int>(maxy));
	for(xpos = 0; xpos < maxx; xpos++){
		for(ypos = 0; ypos < maxy; ypos++){
			for(int i = 0; i < x.size(); i++){
				distance = abs(xpos - x[i]) + abs(ypos - y[i]);
				dmatrix[xpos][ypos] = dmatrix[xpos][ypos] + distance;				
			}
			if(dmatrix[xpos][ypos] < 10000) count++;
		}
	}
	cout << count << endl;
}


