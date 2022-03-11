password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	i -= 1  #改放在這裡，美問一次減少一次
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('帳號封鎖')

		
		