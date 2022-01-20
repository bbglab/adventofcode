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

//Ugly code, but it works !

int main(){

    map<char, int> counter{{'0', -1}, {'1', 1}};

    string line;
    ifstream input_file;
    input_file.open("input.txt");

    vector<string> all_lines;
    int first_step = 0;
    int size_of_word = 0;
    while(getline(input_file, line)) {
        all_lines.push_back(line);
        first_step += counter[line[0]];
        size_of_word = line.size();
    }

    vector<string> oxygen_gen;
    vector<string> co2_scrubber;

    for (const string &s : all_lines) {
        if (first_step >= 0 and s[0] == '1') oxygen_gen.push_back(s);
        else if (first_step < 0 and s[0] == '0') oxygen_gen.push_back(s);
        else co2_scrubber.push_back(s);
    }

    for (int i = 1; i < size_of_word; ++i) {
        if (oxygen_gen.size() > 1) {
            vector<string> oxygen_gen_aux;

            int step = 0;
            for (int j = 0; j < oxygen_gen.size(); ++j) {
                step += counter[oxygen_gen[j][i]];
            }

            for (int j = 0; j < oxygen_gen.size(); ++j) {
                char s = oxygen_gen[j][i];
                if (step >= 0 and s == '1') oxygen_gen_aux.push_back(oxygen_gen[j]);
                else if (step < 0 and s == '0') oxygen_gen_aux.push_back(oxygen_gen[j]);
            }

            oxygen_gen = oxygen_gen_aux;
        }


        if (co2_scrubber.size() > 1) {
            vector<string> co2_scrubber_aux;

            int step = 0;
            for (int j = 0; j < co2_scrubber.size(); ++j) {
                step += counter[co2_scrubber[j][i]];
            }

            for (int j = 0; j < co2_scrubber.size(); ++j) {
                char s = co2_scrubber[j][i];
                if (step >= 0 and s == '0') co2_scrubber_aux.push_back(co2_scrubber[j]);
                else if (step < 0 and s == '1') co2_scrubber_aux.push_back(co2_scrubber[j]);
            }

            co2_scrubber = co2_scrubber_aux;
        }
    }

    long life_support = binary_to_decimal(oxygen_gen[0]) * binary_to_decimal(co2_scrubber[0]);
    cout << life_support << endl;
}