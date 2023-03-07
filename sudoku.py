from colorama import Fore
from datetime import datetime
from time import sleep
from sudoku_scraper import get_puzzle
from sudoku_solver import solve_sudoku
import copy


def print_board(mat):
    for x in range(9):
        if x % 3 == 0:
            print(Fore.RED+"___"*8)
        for y in range(9):
            if y % 3 == 0:
                print(Fore.RED + "|", end=" ")
            if mat[x][y] == 0:
                print(Fore.BLACK + "x", end=" ")
            else:
                print(Fore.BLUE + str(mat[x][y]), end=" ")
        print("")


def print_sol(mat, sol):
    for x in range(9):
        if x % 3 == 0:
            print(Fore.RED+"___"*8)
        for y in range(9):
            if y % 3 == 0:
                print(Fore.RED + "|", end=" ")
            if mat[x][y] == 0:
                print(Fore.GREEN + str(sol[x][y]), end=" ")
            else:
                print(Fore.BLUE + str(sol[x][y]), end=" ")
        print("")


level_url = {
    1: "https://www.nytimes.com/puzzles/sudoku/easy",
    2: "https://www.nytimes.com/puzzles/sudoku/medium",
    3: "https://www.nytimes.com/puzzles/sudoku/hard"
}

print(Fore.BLUE + "------ Today's New York Times Sudoku Puzzle ------")
print(Fore.RED + f":::::: {datetime.date(datetime.now())}")

# get user input for level
url = level_url[int(input(Fore.BLACK +
                          "Which level do you want to try?\n\t(1) Easy\n\t(2) Medium\n\t(3) Hard\n\nEnter a number :"))]

# get the puzzle from url
puzzle = get_puzzle(url)

sleep(2)
print(Fore.MAGENTA + "\n\nTry to solve the puzzle")
print_board(puzzle)

sleep(5)

# deep copy the puzzle problem (it will help to identify the predefined numbers and solved numbers)
ans = copy.deepcopy(puzzle)

input(Fore.LIGHTRED_EX+"\n\nPress Enter to know the solution : ")

# solve the puzzle
solve_sudoku(ans, 0, 0, 9)

print("\n\n")
print(Fore.CYAN+"Printing the solution")
print_sol(puzzle, ans)

print("\n\nTry other levels or Come tomorrow to get new puzzles. Thank you :)")
