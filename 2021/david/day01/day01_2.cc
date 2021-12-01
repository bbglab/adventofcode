#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    string line;
    ifstream input_file;
    input_file.open("input.txt");

    vector<string> lines;
    while(getline(input_file, line)) { lines.push_back(line); }

    int i = 0;
    int j = 1;
    int k = 2;

    vector<int> results;
    while (k < lines.size()) {
        int result = stoi(lines[i]) + stoi(lines[j]) + stoi(lines[k]);
        results.push_back(result);
        ++k; ++j; ++i;
    }

    int count, last = 0;
    for (int i = 0; i <= results.size(); ++i) {
        if (last) {
            count += int(last < results[i]);
        }
        last = results[i];
    }

    cout << count << endl;
}