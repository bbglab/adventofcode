#include <iostream>
#include <vector>

using namespace std;

struct point{
	int x;
	int y;
	int v_x;
	int v_y;
};

struct point read_point(){
	char letter;
	string word;
	struct point res;
	for (int i = 0; i < 9; i++) cin >> letter; 
	cin >> res.x; 
	cin >> letter >> res.y;
	for (int i = 0; i < 11; i++) cin >> letter;
	cin >> res.v_x; 
	cin >> letter >> res.v_y;
	cin >> word;
	return res;
}

bool sort_points_y(struct point a, struct point b){	
	if(a.y == b.y) return a.x < b.x;
	return a.y < b.y;
}

// return position when 6 vertical aligned points appear
int align_points(vector<struct point> points){
	sort(points.begin(), points.end(), sort_points_y);
	bool align = true;;
	for(int i = 0; i < points.size() - 6; i++){
		align = true;
		for(int j = 0; j < 4; j++) align = align and points[i+j+1].x - points[i+j].x == 1;
		if(align) return align;
	}
	return -1;
}

void plot_points(vector<struct point> points){
	int max_x = points[0].x;
	int min_x = points[0].x;
	int min_y;
	int max_y;
	int current = 0;
	sort(points.begin(), points.end(), sort_points_y);
	for(int i = 0; i < points.size(); i++){
		if(points[i].x < min_x) min_x = points[i].x;
                if(points[i].x > max_x) max_x = points[i].x;
	}
	min_y = points.front().y;
	max_y = points.back().y;
	for(int j = min_y - 2; j < max_y + 2; j++){
		for(int i = min_x - 2; i < max_x + 2; i++){
			if(points[current].x == i and points[current].y == j){
				cout << "#";
				while(points[current].x == i and points[current].y == j) current++;
			}
			else{
				cout << ".";
			}
		}
		cout << endl;
	}
}

int main(){
	int iter;
	char letter;
	int value;
	vector<struct point> points;
	while(cin >> letter){
		if(letter != 'p'){
			cout << "Error reading " << letter << endl;
			return 1;
		}
		points.push_back(read_point());
	}
	iter = 0;
	while(iter < 1000000 and align_points(points) < 0){
		for(int i = 0; i < points.size(); i++){
			points[i].x = points[i].x + points[i].v_x;
			points[i].y = points[i].y + points[i].v_y;
		}
		iter++;
	}
	plot_points(points);
	cout << "Result obtained in " << iter << " seconds" << endl;
}

