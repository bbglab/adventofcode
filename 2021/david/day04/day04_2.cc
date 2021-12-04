#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <unordered_set>
using namespace std;

struct Player {
    bool might_win;
    vector<vector<int>> board;
    vector<vector<bool>> marked_board;
};

vector<int> splitByComma(string &line) {
    vector<int> out;
    stringstream ss(line);

    for (int i; ss >> i;) {
        out.push_back(i);
        if (ss.peek() == ',') ss.ignore();
    }

    return out;
}

vector<int> splitBySpace(const string &line) {
    vector<int> out;
    stringstream ss(line);
    for (int i; ss >> i;) {
        out.push_back(i);
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

void check_winner(vector<Player> &players, unordered_set<int> &winners_counter, vector<int> &winners_list) {
    for (int g = 0; g < players.size(); ++g) {
        for (int i = 0; i < players[g].marked_board.size(); ++i) {
            bool line_marked = all_of( players[g].marked_board[i].begin(), players[g].marked_board[i].end(),
                                       []( bool v){ return v; } );
            if (line_marked) {
                if (!winners_counter.count(g)) {
                    winners_counter.insert(g);
                    winners_list.push_back(g);
                }
            }
        }

        for (int i = 0; i < players[g].marked_board.size(); ++i) {
            vector<bool> line_to_inspect;
            vector<int> line_winner;
            for (int j = 0; j < players[g].marked_board[i].size(); ++j) {
                line_to_inspect.push_back(players[g].marked_board[j][i]);
                line_winner.push_back(players[g].board[j][i]);
            }
            bool line_marked = all_of(line_to_inspect.begin(), line_to_inspect.end(), []( bool v){ return v; } );
            if (line_marked) {
                if (!winners_counter.count(g)) {
                    winners_counter.insert(g);
                    winners_list.push_back(g);
                }
            }
        }
    }
}

int main(){

    string line;
    ifstream input_file;
    input_file.open("input.txt");

    getline(input_file, line);

    vector<int> draw_num = splitByComma(line);

    getline(input_file, line);

    vector<Player> players;

    Player usual_player;
    while(getline(input_file, line)) {
        if (line.size() == 0) {
            players.push_back(usual_player);
            usual_player = Player();
        } else {
            vector<int> row = splitByComma(line);
            usual_player.board.push_back(row);

            vector<bool> row_mark(row.size(), false);
            usual_player.marked_board.push_back(row_mark);
        }
    };
    players.push_back(usual_player);

    int last_called;
    unordered_set<int> winners_counter;
    vector<int> winners_list;
    for (int c = 0; c < draw_num.size(); ++c) {
        last_called = draw_num[c];
        for (Player &p : players) {
            for (int i = 0; i < p.board.size(); ++i) {
                for (int j = 0; j < p.board[i].size(); ++j) {
                    if (p.board[i][j] == last_called) {
                        p.marked_board[i][j] = true;
                    }
                }
            }
        }

        check_winner(players, winners_counter, winners_list);
        if (winners_list.size() == players.size())
            break;
    }

    int unmarked = get_unmarked(players[winners_list[winners_list.size() - 1]]);
    cout << unmarked * last_called << endl;
}