# Character Picture Grid
# Project 4.3.1 of Automate the Boring Stuff
# Made by bluelagoon2772, 2020

#Copied list of lists
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x=0
for i in range(0,6):
    y=0
    for v in range(0,9):
        print(grid[y][x],end='')
        y=y+1
    print()
    x+=1
