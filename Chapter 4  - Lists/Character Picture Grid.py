# Character Picture Grid
# Ver 1 - first try. To improve.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotated_list(the_list):
    row = 0
    # loops as many times as long is the inner list
    for i in range(len(the_list[0])):
        # loops as many times as many inner list contains main list
        for j in range(len(the_list) + 1):
            if row > 8:
                print("")
                row = 0
            else:        
                print(the_list[j][i], end = '')
                row += 1

rotated_list(grid)

    

