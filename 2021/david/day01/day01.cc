#include <iostream>
#include <fstream>
using namespace std;

int main(){
    string line;
    ifstream myfile;
    myfile.open("input1.txt");
    bool first = true;
    int count = 0;
    int last;
    while(getline(myfile, line)) {
        if (first) {
            first = false;
            last = stoi(line);
        } else {
            if (last < stoi(line))
                ++count;
            last = stoi(line);
        }
    }

    cout << count << endl;
}