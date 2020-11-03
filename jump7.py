# 1~100中逢7跳过
num = 1
while num <101:
	if num % 7 != 0:            #不为7的倍数
		if num%10 != 7:         #个位数不为7
			if num//10 != 7:    #十位数不为7
				print(num)
	num += 1

