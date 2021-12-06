#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

#include <numeric>
#include <functional>
using namespace std;

vector<int> split_line_comma(string &line) {
    vector<int> out;
    stringstream ss(line);

    for (int num; ss >> num;) {
        out.push_back(num);
        if (ss.peek() == ',') ss.ignore();
    }

    return out;
}

int main(){

    string line;
    ifstream input_file;
    input_file.open("input.txt");

    getline(input_file, line);
    vector<int> states = split_line_comma(line);

    unsigned long long result;

    vector<string> states_count(9,"0");
    for (int i = 0; i < states.size(); ++i) {
        states_count[states[i]] = to_string(stoull(states_count[states[i]]) + 1);
    }

    for (int i = 0; i < 256; ++i) {
        unsigned long long new_states = 0;
        for (int j = 0; j < states_count.size(); ++j) {
            if (j == 0) {
                new_states += stoull(states_count[j]);
                states_count[j] = "0";
            } else {
                states_count[j-1] = states_count[j];
                states_count[j] = "0";
            }
        }

        states_count[6] = to_string(stoull(states_count[6]) + new_states);
        states_count[states_count.size() - 1] =  to_string(stoull(states_count[states_count.size() - 1]) + new_states);
    }

    for (const string i : states_count) result += stoull(i);

    cout << result << endl;
}