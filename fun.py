def draw_rect(w, l, s):
    for j in range(w):
        for k in range(l):
            print(s, end='')
        print(s)


draw_rect(5, 15, '*')
