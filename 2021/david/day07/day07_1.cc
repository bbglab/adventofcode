#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <climits>
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
    vector<int> positions = split_line_comma(line);

    int min_fuel = INT_MAX;
    for (int i = 0; i < positions.size(); ++i) {
        int total = 0;
        for (int j = 0; j < positions.size(); ++j) {
            total += abs(positions[j] - positions[i]);
        }

        min_fuel = (total < min_fuel) ? total : min_fuel;
    }

    cout << min_fuel << endl;
}