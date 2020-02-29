def numberLetterCounts(val):
	words = { 0: '', 1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteenth', 20:'twenty', 30: 'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000: 'thousand'}
	u_str=''
	for limit in range(1, val+1):
		and_v = False
		while True:
			if limit >=1000:
				num = limit // 1000
				print(num)
				limit = limit % 1000
				u_str += words[num] + words[1000]
			
			elif limit >=100 and limit < 1000:
				num = limit //100
				print(num)
				limit = limit % 100
				u_str += words[num] + words[100]
			elif limit >= 10 and limit < 100:
				print(limit)
				num = limit//10
				if num == 0:
					break
				print(num)
			
				limit = limit % (num*10)
				u_str += 'and'+words[num*10]
				and_v = True
			else:
			
				if and_v == False and limit > 0 and len(str(val)) > 1:
					u_str += 'and'+words[limit]
				else:
					u_str += words[limit]
				break
			
			
	return len(u_str)
print(numberLetterCounts(150))