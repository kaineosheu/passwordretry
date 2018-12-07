pw = 'a123456'
count = 3
while count > 0:
	count = count - 1
	input_pw = input('請輸入密碼登入，最多輸入3次密碼: ')
	if pw == input_pw:
		print('登入成功')
		break
	else:
		if count > 0:
			print('密碼錯誤解 還有',count,'機會')
		else:
			print('密碼錯誤')
			print('沒有機會嘗試! 要鎖帳號了拉')
		
	
	


