# 读取文件并处理数据
with open('report.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 分离表头和数据
header = lines[0].strip().split()  # 表头：姓名 语文 数学 ...
data = [line.strip().split() for line in lines[1:]]  # 学生数据

# 转换为字典列表，方便处理
students = []
for row in data:
    student = {
        '姓名': row[0],
        '成绩': [int(score) for score in row[1:]],  # 将成绩转为整数
    }
    student['总成绩'] = sum(student['成绩'])  # 计算总成绩
    student['平均分'] = round(student['总成绩'] / len(student['成绩']), 2)  # 计算平均分
    students.append(student)

# 按总成绩从高到低排序
students.sort(key=lambda x: x['总成绩'], reverse=True)

# 添加名次
for i, student in enumerate(students, 1):
    student['名次'] = i

# 计算每科平均分和总平均分
subjects = header[1:]  # 除去“姓名”的科目列表
subject_totals = [0] * len(subjects)
for student in students:
    for i, score in enumerate(student['成绩']):
        subject_totals[i] += score
subject_avgs = [round(total / len(students), 2) for total in subject_totals]
total_avg = round(sum(subject_avgs) / len(subject_avgs), 2)

# 替换60分以下的成绩为“不及格”
for student in students:
    student['成绩显示'] = [score if score >= 60 else '不及格' for score in student['成绩']]

# 准备输出内容
output_lines = []
# 第一行：科目平均分和总平均分
output_lines.append('名次 姓名 ' + ' '.join(subjects) + ' 总成绩 平均分\n')
output_lines.append('平均分 - ' + ' '.join(map(str, subject_avgs)) + f' - {total_avg}\n')

# 学生数据
for student in students:
    line = (f"{student['名次']} {student['姓名']} " +
            ' '.join(map(str, student['成绩显示'])) +
            f" {student['总成绩']} {student['平均分']}")
    output_lines.append(line + '\n')

# 保存到新文件 result.txt
with open('result.txt', 'w', encoding='utf-8') as file:
    file.writelines(output_lines)

print("处理完成，结果已保存到 result.txt")