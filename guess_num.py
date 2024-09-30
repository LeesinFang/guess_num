<<<<<<< HEAD
import random
start = input('請輸入數字最小值: ')
end = input('請輸入數字最大值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1 #count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜你答對囉')
		print(f'這是你猜的第{count}次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print(f'這是你猜的第{count}次')

=======
import random
r = random.randint(1, 100)
count = 0
while True:
	count = count + 1 #count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜你答對囉')
		print(f'這是你猜的第{count}次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print(f'這是你猜的第{count}次')

>>>>>>> 4badf3d588867a86c17edda08c31063b16add503
