# BMI 計算程式
print ('快看看自己的BMI是否在理想範圍吧！')
height = input('請輸入您的身高（公分）')
height = float(height)
height = height / 100
weight = input('請輸入您的體重（公斤）')
weight = float(weight)
bmi = weight / (height*height)
print('你的BMI為：',bmi)
if bmi < 18.5:
	print('你的體重過輕了耶，多吃點唷')
	print('今天很適合來個下午茶，yum yum')
elif bmi < 24 and bmi >= 18.5:
	print('恭喜！你的體重在正常範圍喔，繼續保持，加油')
elif bmi >= 24 and bmi < 27:
	print('你的體重屬於過重，但是還不算肥胖，加油運動，控制飲食，把體重降到正常範圍吧！')
elif bmi >= 27 and bmi < 30:
	print('你現在屬於輕度肥胖喔，飲食要多加注意，也要多運動')
elif bmi >= 30 and bmi < 35:
	print('你現在是中度肥胖，還是少吃點吧 0.0')
else:
	print('重度肥胖，重度肥胖，重度肥胖！再吃會變成豬的')
