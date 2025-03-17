import random

name = input('请输入您的名字：')

try:
    with open('game.txt', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

scores = {}
for l in lines:
    s = l.split()
    if len(s) >= 1:
        scores[s[0]] = s[1:] + ['0'] * (3 - len(s[1:]))  # 补齐，但不依赖它

score = scores.get(name, ['0', '0', '0'])
game_rounds, min_times, total_times = map(int, score)

# 如果是新玩家或数据异常，min_times 初始化为一个大值
if game_rounds == 0 or min_times == 0:
    min_times = float('inf')  # 或 999

# 显示初始统计
if game_rounds > 0 and min_times != float('inf'):
    avg_times = total_times / game_rounds
else:
    avg_times = 0
print(f'{name}, 你已经玩了{game_rounds}轮，最少{min_times if min_times != float("inf") else 0}次猜对，平均{avg_times:.2f}次猜对')

# 游戏循环
bingo = False
while not bingo:
    num = random.randint(1, 10)
    times = 0
    print('Game Start Now!')
    while True:
        try:
            times += 1
            answer = int(input('Type your number here: '))
            if answer < num:
                print('Too small')
            elif answer > num:
                print('Too big')
            else:
                print('Bingo')
                break
        except ValueError:
            print('请输一个整数！')
            times -= 1

    game_rounds += 1
    if times < min_times:
        min_times = times
    total_times += times
    scores[name] = [str(game_rounds), str(min_times), str(total_times)]

    play = input('请问是否继续游戏？输入yes继续，输入no结束: ').lower()
    if play != 'yes':
        bingo = True

# 保存结果
result = ''
for n in scores:
    result += f"{n} {' '.join(scores[n])}\n"
with open('game.txt', 'w', encoding='utf-8') as f:
    f.write(result.rstrip())

avg_times = total_times / game_rounds  # 再次计算平均次数sen
print(f'\n下次见，bye! {name}, 你已经玩了{game_rounds}轮，最少{min_times}次猜对，平均{avg_times:.2f}次猜对')