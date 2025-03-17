import random
import string

code_All = []
for i in range(0, 10):
    al = list(string.ascii_letters)
    ran = random.sample(al, 8)
    code_Str = ''.join(ran)
    if code_Str in code_All:
        ran = random.sample(al, 8)
        code_Str = ''.join(ran)
    else:
        i += 1
        code_All.append(code_Str)


print(code_All)