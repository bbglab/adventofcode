#include <iostream>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

int binary_to_decimal(string &number) {
    int result = 0;

    int base = 1;

    int len =  number.length();
    for (int i = len - 1; i >= 0; --i) {
        if (number[i] == '1')
            result += base;
        base = base * 2;
    }

    return result;
}

int main(){

    map<char, int> counter{{'0', -1}, {'1', 1}};

    string line;
    ifstream input_file;
    input_file.open("input.txt");

    vector<int> result;
    bool first = true;
    while(getline(input_file, line)) {

        int pos = 0;
        for (const char &c : line) {
            if (first) {
                result.push_back(counter[c]);
            } else {
                result[pos] += counter[c];
                ++pos;
            }
        }

        first = false;
    }

    string gamma = "";
    string epsilon = "";
    for (const int c : result) {
        gamma += to_string(c > 0);
        epsilon += to_string(c < 0);
    }

    long consumption = binary_to_decimal(gamma) * binary_to_decimal(epsilon);
    cout << consumption << endl;


}