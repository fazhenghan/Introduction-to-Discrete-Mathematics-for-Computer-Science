import numpy as np

#matrix = np.random.randint(-1, 2, (5,5))

#print(matrix)

def is16(matrix) :
	listsum = 0
	allsum = 0

	for list in matrix :
		#print('list')
		for nt in list :
			listsum = abs(nt) + listsum
		allsum = listsum + allsum
		listsum = 0
		
	if allsum == 16 :
		return True
	else :
		return False

def issolution(matrix) :

		for i in range(5) :
			for j in range(5) :
				if matrix[i][j] == 1 :
					if i != 0 and j != 0 and i != 5 and j != 5 :
						if matrix[i-1][j-1] == 1 :
							return False
						if matrix[i][j-1] == -1 :
							return False							
						if matrix[i-1][j] == -1 :
							return False		
						if matrix[i+1][j] == -1 :
							return False
						if matrix[i][j+1] == -1 :
							return False
						if matrix[i+1][j+1] == 1 :
							return False
					if i == 0 and j ==0 :
						if matrix[i+1][j] == -1 :
							return False
						if matrix[i][j+1] == -1 :
							return False
						if matrix[i+1][j+1] == 1 :
							return False
					if i != 0 and i != 5 and j == 0 :
						if matrix[i-1][j] == -1 :
							return False					
						if matrix[i+1][j] == -1 :
							return False
						if matrix[i][j+1] == -1 :
							return False
						if matrix[i+1][j+1] == 1 :	
							return False						
					if i == 5 and j == 0 :					
						if matrix[i-1][j] == -1 :
							return False							
						if matrix[i][j+1] == -1 :
							return False	
					if i == 5 and j != 0 and j != 5:	
						if matrix[i-1][j-1] == 1 :
							return False
						if matrix[i][j-1] == -1 :
							return False							
						if matrix[i-1][j] == -1 :
							return False	
						if matrix[i][j+1] == -1 :
							return False
					if i == 5 and j == 5 :
						if matrix[i-1][j-1] == 1 :
							return False
						if matrix[i][j-1] == -1 :
							return False							
						if matrix[i-1][j] == -1 :
							return False
					if i != 0 and i != 5 and j == 5 :
						if matrix[i-1][j-1] == 1 :
							return False
						if matrix[i][j-1] == -1 :
							return False							
						if matrix[i-1][j] == -1 :
							return False	
						if matrix[i+1][j] == -1 :
							return False
					if i == 0 and j == 5 :
						if matrix[i][j-1] == -1 :
							return False							
						if matrix[i+1][j] == -1 :
							return False
					if i ==0 and j != 0 and j != 5 :
						if matrix[i][j-1] == -1 :
							return False							
						if matrix[i+1][j] == -1 :
							return False					
						if matrix[i][j+1] == -1 :
							return False
						if matrix[i+1][j+1] == 1 :
							return False	
					else :
						return True
				if matrix[i][j] == -1 :
					if i != 0 and j != 0 and i != 5 and j != 5 :
						if matrix[i-1][j+1] == -1 :
							return False
						if matrix[i][j-1] == 1 :
							return False							
						if matrix[i-1][j] == 1 :
							return False		
						if matrix[i+1][j] == 1 :
							return False
						if matrix[i][j+1] == 1 :
							return False
						if matrix[i+1][j-1] == -1 :
							return False
					if i == 0 and j == 0 :
						if matrix[i+1][j] == 1 :
							return False
						if matrix[i][j+1] == 1 :
							return False
					if i != 0 and i != 5 and j == 0 :
						if matrix[i-1][j] == 1 :
							return False					
						if matrix[i+1][j] == 1 :
							return False
						if matrix[i][j+1] == 1 :
							return False
						if matrix[i-1][j+1] == -1 :	
							return False					
					if i == 5 and j == 0 :					
						if matrix[i-1][j] == 1 :
							return False							
						if matrix[i][j+1] == 1 :
							return False	
					if i == 5 and j != 0 and j != 5:	
						if matrix[i-1][j+1] == -1 :
							return False
						if matrix[i][j-1] == 1 :
							return False							
						if matrix[i-1][j] == 1 :
							return False	
						if matrix[i][j+1] == 1 :
							return False
					if i == 5 and j == 5 :
						if matrix[i][j-1] == 1 :
							return False							
						if matrix[i-1][j] == 1 :
							return False
					if i != 0 and i != 5 and j == 5 :
						if matrix[i+1][j-1] == -1 :
							return False
						if matrix[i][j-1] == 1 :
							return False							
						if matrix[i-1][j] == 1 :
							return False	
						if matrix[i+1][j] == 1 :
							return False
					if i == 0 and j == 5 :
						if matrix[i][j-1] == 1 :
							return False							
						if matrix[i+1][j] == 1 :
							return False
						if matrix[i+1][j-1] == -1 :
							return False
					if i ==0 and j != 0 and j != 5 :
						if matrix[i][j-1] == 1 :
							return False							
						if matrix[i+1][j] == 1 :
							return False					
						if matrix[i][j+1] == 1 :
							return False
						if matrix[i+1][j-1] == -1 :
							return False		
					else :
						return True
							
while True :
	mt = np.random.randint(-1, 2, (5,5))
	if is16(mt) != True :
		continue		
	elif issolution(mt) != True :
		continue		
	else : 
		print(mt)
		quit()