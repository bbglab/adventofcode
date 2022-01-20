#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

vector<int> split_line(string &line) {
    vector<int> out;
    stringstream ss(line);

    for (string i; ss >> i;) {
        if (i != "->") {
            stringstream ssn(i);
            for (int num; ssn >> num;) {
                out.push_back(num);
                if (ssn.peek() == ',') ssn.ignore();
            }
        }
    }

    return out;
}

void fill_board(vector<vector<int>> &board, int x_1, int x_2, int y_1, int y_2) {
    int max_x = max(x_1, x_2);
    int min_x = min(x_1, x_2);

    int max_y = max(y_1, y_2);
    int min_y = min(y_1, y_2);

    if (x_1 == x_2) {
        for (int j = min_y; j <= max_y; ++j) ++board[j][x_1];
    } else if (y_1 == y_2) {
        for (int j = min_x; j <= max_x; ++j) ++board[y_1][j];
    } else {

        if (x_1 > x_2 and y_1 < y_2) {
            int i = x_1;
            int j = y_1;
            while (i >= x_2 and j <= y_2) {
                ++board[j][i];
                --i; ++j;
            }
        } else if  (x_1 < x_2 and y_1 < y_2) {
            int i = x_1;
            int j = y_1;
            while (i <= x_2 and j <= y_2) {
                ++board[j][i];
                ++i; ++j;
            }
        } else if  (x_1 > x_2 and y_1 > y_2) {
            int i = x_1;
            int j = y_1;
            while (i >= x_2 and j >= y_2) {
                ++board[j][i];
                --i; --j;
            }
        } else if  (x_1 < x_2 and y_1 > y_2) {
            int i = x_1;
            int j = y_1;
            while (i <= x_2 and j >= y_2) {
                ++board[j][i];
                ++i; --j;
            }
        }
    }
}

int main(){

    string line;
    ifstream input_file;
    input_file.open("input.txt");

    vector<vector<int>> board(1000,vector<int>(1000, 0));

    while(getline(input_file, line)) {
        vector<int> floor = split_line(line);
        int x_1 = floor[0];
        int y_1 = floor[1];
        int x_2 = floor[2];
        int y_2 = floor[3];

        fill_board(board, x_1, x_2, y_1, y_2);
    }

    int total = 0;
    for (const vector<int> row : board) {
        for (const int pos : row) {
            total += int(pos >= 2);
            cout << pos << " ";
        }
        cout << endl;
    }
    cout << endl;

    cout << total << endl;
}