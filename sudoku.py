
import numpy as np
def check_for_move(sudoku, row, col, numb):
	for i in range(9):
		if sudoku[row][i]==numb:
			return False

	for i in range(9):
		if sudoku[i][col]==numb:
			return False

	block_row = row-row%3
	block_col = col-col%3
	for i in range(3):
		for j in range(3):
			if sudoku[block_row+i][block_col+j]==numb:
				return False

	return True
#solving by recursive or back tracking logic 
def sudoku_solve(sudoku, row, col):
	if col == 9:
		if row == 8:
			return True
		row += 1
		col = 0
	
	if sudoku[row][col]>0:
		return sudoku_solve(sudoku, row, col+1)	


	for num in range(1,10):
		if check_for_move(sudoku, row, col, num):
			sudoku[row][col] = num
			if sudoku_solve(sudoku, row, col+1):
				return True	
		sudoku[row][col] = 0
	return False

# sudoku=[[0, 0, 0, 8, 0, 0, 0, 5, 0 ],
# 		[0, 0, 8, 0, 4, 0, 0, 9, 0 ],
# 		[5, 7, 3, 1, 0, 0, 0, 0, 4 ],
# 		[0, 0, 0, 0, 0, 8, 0, 0, 0 ],
# 		[0, 1, 0, 4, 0, 0, 0, 6, 3 ],
# 		[0, 0, 0, 5, 6, 0, 9, 0, 0 ],
# 		[0, 6, 9, 0, 0, 0, 0, 3, 1 ],
# 		[0, 0, 1, 0, 0, 0, 0, 7, 2 ],
# 		[0, 0, 0, 6, 1, 0, 5, 0, 0 ]]
# sudoku=[[0, 0, 0, 3, 0, 0, 4, 0, 0 ],
# 		[0, 0, 0, 0, 7, 4, 5, 8, 0 ],
# 		[0, 0, 0, 0, 0, 0, 0, 2, 6 ],
# 		[0, 0, 5, 0, 0, 0, 0, 0, 0 ],
# 		[2, 4, 0, 0, 9, 0, 0, 0, 8 ],
# 		[7, 0, 0, 0, 0, 0, 2, 0, 0 ],
# 		[3, 0, 4, 5, 2, 6, 0, 0, 0 ],
# 		[0, 5, 0, 0, 0, 9, 7, 0, 0 ],
# 		[0, 0, 9, 7, 8, 1, 0, 5, 0 ]]	

np.random.seed(5555)

sudoku=np.random.randint(low=0,high=10,size=(9,9))	
print(sudoku)							
if sudoku_solve(sudoku, 0, 0):
	for m in range(9):
		for n in range(9):
			print(sudoku[m][n], end=" ")
		print()
else:
	print("Unresolved Sudoku")



