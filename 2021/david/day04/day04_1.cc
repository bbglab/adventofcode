#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

struct Player {
    vector<vector<int>> board;
    vector<vector<bool>> marked_board;
};

vector<int> split_line(string &line) {
    vector<int> out;
    stringstream ss(line);

    for (int i; ss >> i;) {
        out.push_back(i);
        if (ss.peek() == ',') ss.ignore();
    }

    return out;
}

int get_unmarked(Player &player) {
    int total = 0;

    for (int i = 0; i < player.board.size(); ++i) {
        for (int j = 0; j < player.board[i].size(); ++j) {
            if (!player.marked_board[i][j]) total += player.board[i][j];
        }
    }

    return total;
}

int check_winner(vector<Player> &players) {
    int unmarked = 0;
    for (Player p : players) {
        for (int i = 0; i < p.marked_board.size(); ++i) {
            bool line_marked = all_of( p.marked_board[i].begin(), p.marked_board[i].end(), []( bool v){ return v; } );
            if (line_marked) {
                return get_unmarked(p);
            }
        }

        for (int i = 0; i < p.marked_board.size(); ++i) {
            vector<bool> line_to_inspect;
            vector<int> line_winner;
            for (int j = 0; j < p.marked_board[i].size(); ++j) {
                line_to_inspect.push_back(p.marked_board[j][i]);
                line_winner.push_back(p.board[j][i]);
            }
            bool line_marked = all_of(line_to_inspect.begin(), line_to_inspect.end(), []( bool v){ return v; } );
            if (line_marked) {
                return get_unmarked(p);
            }
        }
    }

    return unmarked;
}

int main(){

    string line;
    ifstream input_file;
    input_file.open("input.txt");

    getline(input_file, line);

    vector<int> draw_num = split_line(line);

    getline(input_file, line);

    vector<Player> players;

    Player usual_player;
    while(getline(input_file, line)) {
        if (line.size() == 0) {
            players.push_back(usual_player);
            usual_player = Player();
        } else {
            vector<int> row = split_line(line);
            usual_player.board.push_back(row);

            vector<bool> row_mark(row.size(), false);
            usual_player.marked_board.push_back(row_mark);
        }
    };
    players.push_back(usual_player);

    int last_called;
    for (const int &c : draw_num) {
        last_called = c;
        for (Player &p : players) {
            for (int i = 0; i < p.board.size(); ++i) {
                for (int j = 0; j < p.board[i].size(); ++j) {
                    if (p.board[i][j] == last_called) {
                        p.marked_board[i][j] = true;
                    }
                }
            }
        }

        int unmarked = check_winner(players);
        if (unmarked) {
            long total = unmarked * last_called;
            cout << total << endl;
            break;
        }
    }
}