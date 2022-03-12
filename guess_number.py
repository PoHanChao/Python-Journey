#randomly generate 1~100
#let the user input a number
#if the user guess the right number, show"bingo"
#if the umber is wrong, tell the user f it's greater or smaller
import random
start = int(input('The start range: '))  #the player can decide the range
end = int(input('The end range: '))
r = random.randint(start, end)
i=5
while True:
	num = input('Please guess the number: ')
	num = int(num)
	i -= 1
	if i > 0:
		if num == r:
			print('bnigo')
			break
		elif num > r and num >= start and num <= end:
			print('choose a smaller number')		
			print()
		elif num < r and num >= start and num <=end:
			print('choose a greater number')
			print()
			print()
		else:
			print('The number i between', start, 'and', end)
			print()	
		print('You still have', i,'more chance') 
	else:
		print('Mission failed')
		print('The number is:', r)
		break

