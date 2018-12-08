#include <iostream>
#include <vector>
using namespace std;

struct work{
	char id;
	int prev;
	vector<struct work *> next;
};

bool compare( struct work a, struct work b){
	return a.id < b.id;
}

int main(){
	string word;
	char a, b;
	vector<struct work> works = vector<struct work>('Z' - 'A' + 1);
	for(int i = 0; i < works.size(); i++) works[i].id = '0';
	while(cin >> word >> a >> word >> word >> word >> word >> word >> b >> word >> word){
		if(word[5] != '.') cerr << "Error reading, last word: " << word << endl;
		works[a - 'A'].id = a;
		works[a - 'A'].next.push_back(&works[b - 'A']);
		works[b - 'A'].id = b;
		works[b - 'A'].prev++;
	}
	sort(works.begin(), works.end(), compare);

	int current = 0;
	while(works.size() > current){
		if(works[current].id == '0'){
			//works.erase(works.begin() + current);
			current++;
		}
		else{
			if(works[current].prev == 0){
				cout << works[current].id;
				for(int i = 0; i < works[current].next.size(); i++) works[current].next[i]->prev--;
				works[current].id = '0';
				current = 0;
			}
			else{
				current++;
			}
		}
//		cout << works.size() << " - " << current << endl;
	}
	cout << endl;
}

