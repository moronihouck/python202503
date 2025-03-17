import random

card = []
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['s', 'h', 'd', 'c']

for i in range(len(suit)):
    for j in range(len(nums)):
        card.append(suit[i] + nums[j])
card.append('red_joker')
card.append('black_joker')
player1 = []
player2 = []
player3 = []

# 发牌，每个玩家17张，发一张然后从card中删除，保证没有重复的
for i in range(0,17):
    i += 1
    player1.append(random.choice(card))
    card.remove(player1[-1])
    player2.append(random.choice(card))
    card.remove(player2[-1])
    player3.append(random.choice(card))
    card.remove(player3[-1])

bottom_cards = card # 剩余的3张底牌
print('玩家 1 的牌：', player1)
print('玩家 2 的牌：', player1)
print('玩家 3 的牌：', player1)
print('底牌3张：', bottom_cards)


