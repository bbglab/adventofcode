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
    vector<int> results;
    while (i < lines.size() - 2) {
        int result = stoi(lines[i]) + stoi(lines[i+1]) + stoi(lines[i+2]);
        results.push_back(result);
        ++i;
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