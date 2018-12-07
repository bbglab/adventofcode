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
	
	while(cin>> xpos >> symbol >> ypos){
		x.push_back(xpos);
		y.push_back(ypos);
		if(maxx < xpos)  maxx = xpos;
		if(maxy < ypos) maxy = ypos;
	}
	maxx = maxx + 2;
	maxy = maxy +2;
	vector<vector<int> > dmatrix = vector<vector<int> >(maxx, vector<int>(maxy, (maxy+maxx)));
	vector<vector<int> > posmatrix = vector<vector<int> >(maxx, vector<int>(maxy));
	vector<int> count = vector<int>(x.size());
	for(xpos = 0; xpos < maxx; xpos++){
		for(ypos = 0; ypos < maxy; ypos++){
			for(int i = 0; i < x.size(); i++){
				distance = abs(xpos - x[i]) + abs(ypos - y[i]);
				if(dmatrix[xpos][ypos] == distance){
					posmatrix[xpos][ypos] = -1;
				}
				else{
					if(dmatrix[xpos][ypos] > distance){
						posmatrix[xpos][ypos] = i;
						dmatrix[xpos][ypos] = distance;
					}
				}				
			}
			if(xpos == 0 or ypos == 0 or xpos == maxx-1 or ypos == maxy-1) count[posmatrix[xpos][ypos]] = -1*maxx*maxy;
			if(posmatrix[xpos][ypos] != -1) count[posmatrix[xpos][ypos]]++;
		}
	}
	maxx = 0;
	for(int i = 0; i < x.size(); i++){
		if(count[i] > maxx) maxx = count[i];
	}
	cout << maxx << endl;
}


