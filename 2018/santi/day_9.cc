#include <iostream>
#include <vector>
using namespace std;

struct marble{
	int id;
	struct marble *prev;
	struct marble *next;
};

int main(){
	int players;
	int last;
	string word;
	cin >> players >> word >> word >> word >> word >> word >> last;
	struct marble *current = new(struct marble);
	struct marble *aux;
	current->id = 0;
	current->prev = current;
	current->next = current;
	vector<long int> scores = vector<long int>(players);
	int i = 1;
	while (i < last + 1){
		if(i % 23 == 0){
			scores[(i%players)] = scores[(i%players)] + i;
			for(int j = 0; j < 6; j++){
				current = current->prev;
			}
			scores[(i%players)] = scores[(i%players)] +  current->prev->id;
			aux = current->prev;
			current->prev = aux->prev;
			aux->prev->next = aux->next;
			delete(aux);
		}
		else{
			aux = new(struct marble);
			aux->id = i;
			current = current->next;
			aux->next = current->next;
			aux->prev = current;
			current->next->prev = aux;
			current->next = aux;
			current = aux;
		}
		i++;
	}
	i = 0;;
	for(int j = 0; j < players; j++){
		if(scores[i] < scores[j]) i = j;
	}
	cout << scores[i] << endl;
}

