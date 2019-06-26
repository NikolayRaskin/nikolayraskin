def flag(N):
	"""Japanese flag"""

	#rectangle str
	rect = '#' + '#'*(N * 3) + '#\n' 
	for i in range(N*2):
	 	rect += '#' + ' '*(N * 3) + '#\n'
	rect += '#' + '#'*(N * 3) + '#\n'
	
	#split rectangle str to list
	list = rect.split('\n')
	
	#changing strings using slices
	line = 1
	count = 2
	newLine=0
	while line <= N:
		for i in range(int(N/2)+line, N + N - int(N/2)+line):
			#first line
			if line == 1:
				list[i] = list[i][0:N+int(N/2)] +'**' +list[i][N+int(N/2)+2:]
				line += 1
			#befor middle
			elif line <= N/2:
				list[i] = list[i][0:N-line+int(N/2)+1] +'*'+ 'o'*count +'*' +list[i][N+N+line-int(N/2)+1:]
				line += 1
				count += 2
			#after middle
			elif line >= N/2:
				newCount = count - 2
				newLine += int(N/2)
				list[i] = list[i][0:N-newLine+int(N/2)+1] +'*'+ 'o'*newCount +'*' +list[i][N+N+newLine-int(N/2)+1:]
				newLine -= int(N/2)+1
				count -= 2
				line += 1
			#last line
			elif line == N:
				list[i] = list[i][0:N+line] +'**' +list[i][N+N+1:]
				line += 1

	finalStr = ''
	for i in range(len(list)):
		finalStr += list[i]+'\n'
	
	return finalStr

class ArgumentError(Exception):
    pass

try:
	inputValue = input('N = ')
	inputValue = int(inputValue)
	if inputValue % 2 == 0 and inputValue > 0:
		print(flag(inputValue))
	else:
		raise ArgumentError
except ValueError:
	print('The input N shall be an integer type')
except ArgumentError:
	print('The input N shall be an positive and even number')







