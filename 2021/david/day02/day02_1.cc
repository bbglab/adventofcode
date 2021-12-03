#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

vector<string> split_line(const string &line) {
    vector<string> out;
    stringstream ss(line);
    string temp;
    while (ss >> temp)
        out.push_back(temp);
    return out;
}

int main(){

    map<string, int> instructions{{"up", -1}, {"down", 1}};

    string line;
    ifstream input_file;
    input_file.open("input.txt");

    int depth, horizontal_pos = 0;
    while(getline(input_file, line)) {

        vector<string> out = split_line(line);
        string move = out[0];
        int value = stoi(out[1]);

        if (move == "forward")
            horizontal_pos += value;
        else depth += instructions[move] * value);
    }

    long long result = depth * horizontal_pos;
    cout << result << endl;
}