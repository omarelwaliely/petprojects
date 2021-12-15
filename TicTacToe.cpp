#include <iostream>
using namespace std;
bool check(char **, int, int, char);
char **createboard(char **arr)
{
    for (int i = 0; i < 13; i++)
    {
        for (int j = 0; j < 19; j++)
        {
            if (i % 4 == 0)
            {
                arr[i][j] = '=';
            }
            else if (j % 6 == 0)
            {
                arr[i][j] = '|';
            }
            else
            {
                arr[i][j] = ' ';
            }
        }
    }
    return arr;
}
char **update(char **arr, int player, int y, bool &win)
{
    if (player == -1)
    {
        arr[2][3] = '1';
        arr[2][9] = '2';
        arr[2][15] = '3';
        arr[6][3] = '4';
        arr[6][9] = '5';
        arr[6][15] = '6';
        arr[10][3] = '7';
        arr[10][9] = '8';
        arr[10][15] = '9';
        return arr;
    }
    if (y < 0 || y > 9)
    {
        while (y < 0 || y > 9)
        {
            cout << "Choice is not valid, enter a choice from 1-9: ";
            cin >> y;
        }
    }
    char current = 'X';
    if (player == 2)
    {
        current = 'O';
    }
    bool flag = false;
    do
    {
        switch (y)
        {
        case 1:
            if (arr[2][3] == ' ')
            {
                arr[2][3] = current;
                if ((check(arr, 2, 9, current) && check(arr, 2, 15, current)) || ((check(arr, 6, 3, current) && check(arr, 10, 3, current))) || (check(arr, 6, 9, current) && check(arr, 10, 15, current)))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        case 2:
            if (arr[2][9] == ' ')
            {
                arr[2][9] = current;
                if ((check(arr, 2, 3, current) && check(arr, 2, 15, current)) || ((check(arr, 6, 9, current) && check(arr, 10, 9, current))))
                {
                    win = true;
                }
                flag = true;
            }

            break;
        case 3:
            if (arr[2][15] == ' ')
            {
                arr[2][15] = current;
                if ((check(arr, 2, 3, current) && check(arr, 2, 9, current)) || ((check(arr, 6, 15, current) && check(arr, 10, 15, current))) || (check(arr, 6, 9, current) && check(arr, 10, 3, current)))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        case 4:
            if (arr[6][3] == ' ')
            {
                arr[6][3] = current;
                if ((check(arr, 6, 9, current) && check(arr, 6, 15, current)) || ((check(arr, 2, 3, current) && check(arr, 10, 3, current))))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        case 5:
            if (arr[6][9] == ' ')
            {
                arr[6][9] = current;
                if ((check(arr, 6, 3, current) && check(arr, 6, 15, current)) || ((check(arr, 2, 9, current) && check(arr, 10, 9, current))) || (check(arr, 2, 3, current) && check(arr, 10, 15, current)) || (check(arr, 2, 15, current) && check(arr, 10, 3, current)))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        case 6:
            if (arr[6][15] == ' ')
            {
                arr[6][15] = current;
                if ((check(arr, 6, 3, current) && check(arr, 6, 9, current)) || ((check(arr, 2, 15, current) && check(arr, 10, 15, current))))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        case 7:
            if (arr[10][3] == ' ')
            {
                arr[10][3] = current;
                if ((check(arr, 10, 9, current) && check(arr, 10, 15, current)) || ((check(arr, 2, 3, current) && check(arr, 6, 3, current))) || (check(arr, 6, 9, current) && check(arr, 2, 15, current)))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        case 8:
            if (arr[10][9] == ' ')
            {
                arr[10][9] = current;
                if ((check(arr, 10, 3, current) && check(arr, 10, 15, current)) || ((check(arr, 2, 9, current) && check(arr, 6, 9, current))))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        case 9:
            if (arr[10][15] == ' ')
            {
                arr[10][15] = current;
                if ((check(arr, 10, 9, current) && check(arr, 10, 3, current)) || ((check(arr, 2, 15, current) && check(arr, 6, 15, current))) || (check(arr, 6, 9, current) && check(arr, 2, 3, current)))
                {
                    win = true;
                }
                flag = true;
            }
            break;
        }
        if (!flag)
        {
            cout << "That space is already full choose a different one" << endl;
            cin >> y;
        }
    } while (!flag);
    return arr;
}
void printboard(char **board)
{
    for (int i = 0; i < 13; i++)
    {
        for (int j = 0; j < 19; j++)
        {
            cout << board[i][j];
        }
        cout << endl;
    }
}
bool check(char **board, int x, int y, char z)
{
    return (board[x][y] == z);
}

int main()
{
    char **arr;
    char **ref;
    arr = new char *[13];
    ref = new char *[13];
    for (int i = 0; i < 13; i++)
    {
        arr[i] = new char[19];
        ref[i] = new char[19];
    }
    bool flag = false;
    arr = createboard(arr);
    ref = createboard(ref);
    ref = update(ref, -1, -1, flag);
    int choice = 0;
    printboard(arr);
    int i = 1;
    do
    {
        cout << "Player" << i << ": type a number from 1-9, or type 0 to see a reference board." << endl;
        cin >> choice;
        switch (choice)
        {
        case 0:
        {
            printboard(ref);
            break;
        }
        default:
            arr = update(arr, i, choice, flag);
            if (flag)
            {
                break;
            }
            printboard(arr);
            if (i == 1)
            {
                i = 2;
            }
            else
            {
                i = 1;
            }
            break;
        }
        if (flag)
        {
            char choice;
            printboard(arr);
            cout << "Player" << i << " wins!\nWould you like to play again?, (Y or N): ";
            cin >> choice;
            choice = toupper(choice);
            if (choice == 'Y')
            {
                flag = false;
                createboard(arr);
                printboard(arr);
            }
        }
    } while (!flag);

    return 0;
}