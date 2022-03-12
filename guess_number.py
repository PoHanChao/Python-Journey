#randomly generate 1~100
#let the user input a number
#if the user guess the right number, show"bingo"
#if the umber is wrong, tell the user f it's greater or smaller
import random
r = random.randint(1, 100)
i=5
while True:
	num = input('Please guess the number: ')
	num = int(num)
	i -= 1
	if i > 0:
		if num == r:
			print('bnigo')
			break
		elif num > r and num >= 1 and num <=100:
			print('choose a smaller number')		
			print()
		elif num < r and num >= 1 and num <=100:
			print('choose a greater number')
			print()
			print()
		else:
			print('The number i between 1~100')
			print()	
		print('You still have', i,'more chance') 
	else:
		print('Mission failed')
		print('The number is:', r)
		break

