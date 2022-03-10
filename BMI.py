#BMI
h = input('What is your height(cm): ')
w = input('What is your weight(kg): ')
h = float(h)
w = float(w)
bmi = w/(h/100)**2
print('Your BMI is:', bmi)

if bmi < 18.5:
	print('Eat more, you are too thin')
elif bmi >= 18.5 and bmi < 24 :
	print('Nice body')
elif bmi >= 24 and bmi < 27 :
	print('You can loose some weight')
elif bmi >= 27 and bmi < 30 :
	print('You are a little fat')
elif bmi >= 30 and bmi < 35 :
	print('You are ... fat')
else:
	print('You are really fat')



