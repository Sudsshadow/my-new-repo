score = int(input())
if 0 <= score <60:
    level = 'D'
elif 60 <= score < 80:
    level = 'C'
elif 80 <= score < 90:
    level = 'B'
elif 90 <= score < 100:
    level = 'A'
elif score == 100:
    level = 'S'
else:
    level = '请输入0~100之间的分数'
print(level)
