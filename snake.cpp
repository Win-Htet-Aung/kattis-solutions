#include <iostream>
#include <chrono>
#include <thread>
#include <cstdlib>
#include <ctime>
#include <conio.h>

using namespace std;
using namespace std::this_thread; // sleep_for, sleep_until
using namespace std::chrono; // nanoseconds, system_clock, seconds

int main() {
    int row = 30, col = 40;
    char board[row][col];
    int snake[1200][2];
    int next_step[2];
    int snake_length = 3;
    char direction = 'e';

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            board[i][j] = ' ';
        }
    }

    board[0][0] = 'O';
    board[0][1] = 'O';
    board[0][2] = 'O';

    snake[0][0] = 0;
    snake[0][1] = 0;
    snake[1][0] = 0;
    snake[1][1] = 1;
    snake[2][0] = 0;
    snake[2][1] = 2;

    bool game_over = false;

    srand((int) time(0));

    int food_row = (rand() % 30) - 1;
    int food_col = (rand() % 40) - 1;
    bool food_ok = false;

    while (!food_ok) {
        for (int i = 0; i < snake_length; i++) {
            if (snake[i][0] == food_row and snake[i][1] == food_col) {
                food_row = (rand() % 30) - 1;
                food_col = (rand() % 40) - 1;
                break;
            }
            else if (i == snake_length - 1) {
                food_ok = true;
            }
        }
    }

    board[food_row][food_col] = 'X';
    
    while (!game_over) {
        if (kbhit()) {
            char c = getch();
            if (c == 'i' and direction != 's') {
                direction = 'n';
            }
            else if (c == 'j' and direction != 'e') {
                direction = 'w';
            }
            else if (c == 'k' and direction != 'n') {
                direction = 's';
            }
            else if (c == 'l' and direction != 'w') {
                direction = 'e';
            }
        }

        cout << "##########################################\n";
        for (int i = 0; i < row; i++) {
            cout << '#';
            for (int j = 0; j < col; j++) {
                cout << board[i][j];
            }
            cout << "#\n";
        }
        cout << "##########################################\n";
        sleep_for(milliseconds(180));
        system("cls");

        if (direction == 'e') {
            next_step[1] = snake[snake_length - 1][1] + 1;
            next_step[0] = snake[snake_length - 1][0];
        }
        else if (direction == 's') {
            next_step[1] = snake[snake_length - 1][1];
            next_step[0] = snake[snake_length - 1][0] + 1;
        }
        else if (direction == 'w') {
            next_step[1] = snake[snake_length - 1][1] - 1;
            next_step[0] = snake[snake_length - 1][0];
        }
        else if (direction == 'n') {
            next_step[1] = snake[snake_length - 1][1];
            next_step[0] = snake[snake_length - 1][0] - 1;
        }

        if (next_step[0] == food_row and next_step[1] == food_col) {
            snake_length++;
            snake[snake_length - 1][0] = next_step[0];
            snake[snake_length - 1][1] = next_step[1];
            board[snake[snake_length - 1][0]][snake[snake_length - 1][1]] = 'O';

            food_ok = false;

            while (!food_ok) {
                for (int i = 0; i < snake_length; i++) {
                    if (snake[i][0] == food_row and snake[i][1] == food_col) {
                        food_row = (rand() % 30) - 1;
                        food_col = (rand() % 40) - 1;
                        break;
                    }
                    else if (i == snake_length - 1) {
                        food_ok = true;
                    }
                }
            }

            board[food_row][food_col] = 'X';
        }
        else {
            board[snake[0][0]][snake[0][1]] = ' ';
            for (int i = 0; i < snake_length - 1; i++) {
                snake[i][0] = snake[i + 1][0];
                snake[i][1] = snake[i + 1][1];
            }
            snake[snake_length - 1][0] = next_step[0];
            snake[snake_length - 1][1] = next_step[1];
            board[snake[snake_length - 1][0]][snake[snake_length - 1][1]] = 'O';
        }

    }
    
}
