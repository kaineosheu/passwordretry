pw = 'a123456'
count = 0
while True:
	input_pw = input('請輸入密碼登入，最多輸入3次密碼: ')
	count = count + 1
	if pw == input_pw:
		print('登入成功')
		break
	total = 3 - count
	print('密碼錯誤解 還有',total,'機會')
	if total == 0:
		break



