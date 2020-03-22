# Character Picture Grid
# Project 4.3 of Automate the Boring Stuff
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

y=0
for i in grid:
    x=0
    for v in range(0,6):
        print(grid[y][x],end='')
        x=x+1
    print()
    y+=1

