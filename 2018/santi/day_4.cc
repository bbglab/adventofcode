#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct time{
	int date;
	int time;
	int state;
};
struct guard{
	int id;
	vector<int> timestamp;
	int asleep;
	int aminute;
};
bool compare(struct time i, struct time j){
	if(i.date != j.date){
		return (i.date < j.date);
	}
	return (i.time < j.time);
}
struct time read_event(){
	int number;
	char symbol;
	string word;
	struct time current;
	//Date
	cin >> number >> symbol >> number;
	current.date = 100*number;
	cin >> symbol >> number;
	current.date = current.date + number;
	//Hour
	cin >> number >> symbol;
	if(number == 23){
		cin >> number;
		current.time = number + 100;
	}
	else{
		cin >> number;
                current.time = number;
	}
	//State
	cin >> symbol >> word;
	if(word[0] == 'G'){
		cin >> symbol >> number >> word >> word;
		current.state = number;
	}
	else{
		if(word[0] == 'f'){
			cin >> word;
			current.state = -1;
		}
		else{
			if(word[0] == 'w'){
				cin >> word;
				current.state = -2;
			}
			else{
				cerr << "Unexpected read: -" << word << "-" << endl;
			}
		}
	}
	return current;
}

int main(){
	char symbol;
	vector<struct time> events;
	int guard, start;
	map<int, struct guard> mguards;
	while (cin >> symbol){
		if(symbol == '['){
			events.push_back(read_event());
		}
		else{
			cerr << "Bad read" << endl;
		}
	}
	sort(events.begin(), events.end(), compare);
	for (int i=0; i < events.size(); i++){
		if(events[i].state > -1){//Guard
			guard = events[i].state;
			if(mguards.count(guard) == 0){
				mguards[guard].id = guard;
				mguards[guard].timestamp = vector<int>(60,0);
			}
		}
		else{
			if(events[i].state == -1){//Fall asleep
				start = events[i].time;
			}
			else{
				if(events[i].state == -2){//Wakes up
					for(int j = start; j < events[i].time; j++){
						mguards[guard].timestamp[j]++;
					}
				}
				else{
					cerr << "Error reading " << events[i].state << endl;
				}
			}
		}
	}
	start = 0;
	guard = 0;
	int guard2;
	int time2 = 0;
	for(map<int, struct guard>::iterator i = mguards.begin(); i != mguards.end(); ++i){
		i->second.aminute = 0;
		i->second.asleep = 0;
		for(int j = 0; j <60; j++){
			if(i->second.timestamp[j] > i->second.timestamp[i->second.aminute]){
				i->second.aminute = j;
			}
			i->second.asleep = i->second.asleep + i->second.timestamp[j];
		}
		if(i->second.asleep > start){
			start = i->second.asleep;
			guard = i->first;
		}
		if(i->second.timestamp[i->second.aminute] > time2){
			time2 = i->second.timestamp[i->second.aminute];
			guard2 = i->first;
		}
	}
	cout << mguards[guard].aminute * guard << endl;
	cout << mguards[guard2].aminute * guard2 << endl;
}


