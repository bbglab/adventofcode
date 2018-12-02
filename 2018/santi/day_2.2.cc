#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main(){
	string current;
	vector<string> words;
	while (cin >> current){
		words.push_back(current);
	}
	int score;
	for (int i = 0; i < words.size(); i++){
		for(int j = i; j < words.size(); j++){
			score = 0;
			for(int k = 0; k < words[i].size(); k++){
				if(words[i].at(k) == words[j].at(k)) score++;
			}
			if(score == words[i].size() -1){
				cout << words[i] << endl << words[j] << endl;
				for(int k = 0; k < words[i].size(); k++){
					if(words[i].at(k) == words[j].at(k)) cout << words[i].at(k);
				}
				cout << endl;
				return(1);
			}
		}
	}
}

