import collections

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 ["1",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

cols = collections.defaultdict(set)
rows = collections.defaultdict(set)

for i in range(9):
    for j in range(9):
        if (board[i][j] =="."):
            continue
        
        if(board[i][j] in cols and board[i][j] in rows):
            print("invalid")
            break

        cols[j].add(board[i][j])
        rows[i].add(board[i][j])

name = "iqbal"
#print(id(name))
#print(id(name))
name = name + "water"
#print(id(name))

length = len(board)

#print(length)
#print(board[length-1])
#print(board[length])
 
name_dict ={}

name_dict["name", 10, 42, "water"] = ["identity", "what", "name", 100]
#print(name_dict)

list_comp = [[i+j for i in cols] for j in rows]
print(list_comp)
