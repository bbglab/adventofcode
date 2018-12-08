#include <iostream>
#include <vector>
using namespace std;

struct work{
	char id;
	int prev;
	int time;
	bool free;
	vector<int> next;
};

bool compare( struct work a, struct work b){
	return a.id < b.id;
}

int main(){
	string word;
	char a, b;
	int workers;
	int todo = 0;
	int time = 0;
	vector<struct work> works = vector<struct work>('Z' - 'A' + 1);
	for(int i = 0; i < works.size(); i++) works[i].id = '0';
	while(cin >> word >> a >> word >> word >> word >> word >> word >> b >> word >> word){
		if(word[5] != '.') cerr << "Error reading, last word: " << word << endl;
		works[a - 'A'].id = a;
		works[a - 'A'].time = a - 'A' + 60;
		works[a - 'A'].next.push_back(b - 'A');
		works[b - 'A'].id = b;
		works[b - 'A'].prev++;
		works[b - 'A'].time = b - 'A' + 60;
	}
	for(int i = 0; i < works.size(); i++) if(works[i].id != '0') {
		todo++;
		works[i].free = true;
	}
	int current = 0;
	while(todo > 0){
		workers = 5;
		for(int i = 0; i < works.size(); i++) works[i].free = true;
		for (current = 0; current < works.size(); current++){
			if(works[current].id != '0'){
				if(works[current].prev == 0 and works[current].free){
					if(works[current].time == 0){
						for(int i = 0; i < works[current].next.size(); i++){
							works[works[current].next[i]].prev--;
							works[works[current].next[i]].free = false;
						}
						works[current].id = '0';
						todo--;
					}
					else{
						if(workers > 0){
							works[current].time--;
							workers--;
						}
					}
				}
			}
		}
		time++;
	}
	cout << time << endl;
}

