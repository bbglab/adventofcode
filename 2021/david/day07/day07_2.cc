#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <climits>
#include <bits/stdc++.h>

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

    int max = *max_element(positions.begin(), positions.end());
    int min = *min_element(positions.begin(), positions.end());

    int num = min;
    vector<int> after_positions;
    while (num <= max) {
        after_positions.push_back(num);
        ++num;
    }

    int min_fuel = INT_MAX;
    for (int i = 0; i < after_positions.size(); ++i) {
        int total = 0;

        for (int j = 0; j < positions.size(); ++j) {
            int n = abs(after_positions[i]-positions[j]);
            total += (n * (n+1))/2;

            if (total > min_fuel) break;
        }

        min_fuel = (total < min_fuel) ? total : min_fuel;
    }

    cout << min_fuel << endl;
}