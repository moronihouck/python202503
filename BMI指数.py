print('您的体重（公斤）：')
weight = float(input())
print('您的身高（米）：')
height = float(input())
bmi = weight / (height * height)
if bmi < 18.5:
    print('BMI:%.2f 您的体重偏轻' % bmi)
elif 18.5 <= bmi < 24:
    print('BMI:%.2f 您的体重正常' % bmi)
else:
    print('BMI:%.2f 您的体重偏重' % bmi)
