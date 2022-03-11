password = 'a123456'
i = 3 #
while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		i -= 1  #i要放在print之前，這樣才會有"剩下i-1"次
		print('密碼錯誤，還有', i, '次機會')
		if i == 0:
			break

		