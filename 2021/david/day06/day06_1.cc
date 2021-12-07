#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
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

    int result;

    for (int i = 0; i < 80; ++i) {
        int new_state = 0;
        for (int j = 0; j < states.size(); ++j) {
            if (states[j] == 0) {
                states[j] = 6;
            } else {
                --states[j];
                new_state += int(states[j] == 0);
            }
        }

        result = states.size();

        while (new_state > 0) {
            states.push_back(9);
            --new_state;
        }
    }

    cout << result << endl;
}