#include <iostream>
#include <vector>
using namespace std;


int main(){
	int serial, x_max, y_max, max, score;
	//vector<vector<int> > matrix = vector<vector<int>(300)>(300);
	cin >> serial;

	max = -99999;
	for(int i = 0; i < 300 - 2; i++){
		for(int j = 0; j < 300 -2 ; j++){
			score = 0;
			for(int k = 0; k < 3; k++){
				for(int l = 0; l < 3; l++){
					score = score + ((((i+k+11)*(j+l+1)+serial)*(i+k+11)/100)%10)-5;
				}
			}
			if(score > max){
				x_max = i + 1;
				y_max = j + 1;
				max = score;
			}
		}
	}
	cout << x_max << " , " << y_max << " : " << max << endl;
}



