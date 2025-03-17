import random

card = []
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['s', 'h', 'd', 'c']

for i in range(len(suit)):
    for j in range(len(nums)):
        card.append(suit[i] + nums[j])

card.append('red_joker')
card.append('black_joker')
random.shuffle(card) # 洗乱手牌
last_card = card[-3:] # 留下3张底牌
card = card[:-3] # 重新生成手牌

p1 = card[::3]
p2 = card[1::3]
p3 = card[2::3]
#print(last_card)
print(p1)
print(card)