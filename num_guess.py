from random import randint

bingo = 0
guess_times = 0
rd = 0
while not bingo:
    num = randint(1, 10)
    print(num)
    guess = int(input('请猜一个1~10的数字：'))
    guess_times += 1
    print(guess)
    print(guess_times)

    if guess > num:
        print('您说大了！')
    elif guess < num:
        print('您说小了！')
    else:
        print('bingo!')
        rd += 1
        ave = int(guess_times / rd)
        print(f"您平均每轮猜测次数为{ave}次，目前总共游戏{rd}轮。")
        play = input('请问是否继续游戏？输入yes继续，输入no结束: ')
        if play == 'yes':
            bingo = False
        else:
            print('\n下次见，bye!')
            bingo = True
