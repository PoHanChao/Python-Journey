driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能說有或沒有')
	raise SystemExit


age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('Good for you')
	else:
		print('你怎麼有開過車')
elif driving == '沒有':
	if age >= 18:
		print('去考駕照')
	else:
		print('等長大就可以考了')
