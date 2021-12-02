#include <iostream>
#include <fstream>
using namespace std;

int main(){
    string line;
    ifstream input_file;
    input_file.open("input.txt");
    int count, last = 0;
    while(getline(input_file, line)) {
        if (last) {
            count += int(last < stoi(line));
        }

        last = stoi(line);
    }

    cout << count << endl;
}
