def isValidSudoku(board):
    # row & col check
    for i in range(9):
        row_nums = set()
        col_nums = set()
        for j in range(9):
            a = board[i][j]
            b = board[j][i]
            if a != '.':
                if a not in row_nums:
                    row_nums.add(a)
                else:
                    # return False
                    print('false')
                    print(i, j)
            if b != '.':
                if b not in col_nums:
                    col_nums.add(b)
                else:
                    # return False
                    print('false')
                    print(i, j)
                
    # sub-box check
    sub = {}
    for i in range(9):
        if i % 3 == 0:
            sub = {}
        for j in range(9):
            a = board[i][j]
            if a != '.':
                if a not in sub:
                    sub[a] = [j]
                else:
                    found_js = sub[a]
                    
                    for k in found_js:
                        if (j // 3) == (k // 3):
                            print(False)
                            print(i, j, a)

                    sub[a].append(j)

            
    
                
    # return True
    print('true')
board = [
    [".",".",".",   "2",".",".",    ".",".","."],
    [".",".","5",   ".","1","8",    ".",".","."],
    [".",".",".",   "4",".","3",    ".",".","."],

    [".",".",".",   ".",".","1",    ".",".","5"],
    [".","5",".",   ".",".",".",    ".",".","1"],
    [".",".",".",   ".",".",".",    ".","1","."],

    [".",".",".",   ".","3",".",    ".",".","."],
    [".","7",".",   ".","5",".",    ".",".","."],
    [".",".",".",   ".",".",".",    ".","2","3"]
    ]
isValidSudoku(board)

                
            
    