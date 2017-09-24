#-*- coding=utf-8 -*-
import random

ai_input = random.choice(range(3))
user_input = int(input('请输入：剪刀(1)石头(2)布(3):'))
WIN_INFO = '😆\t赢了，你真的是太厉害了！'
LOSE_INFO =  '😭\t输了,不要走，洗洗手接着来，决战到天亮！'
DOGFALL_INFO = '😯\t啊哦，平局，要不再来一局？'

def _translate(_output):
    log = ['剪刀', '石头', '布']
    return log[_output]

if (user_input > 3) or (user_input <1):
    print('亲，请输入1,2,3\t 👌')
else:
    if (user_input == 1 and ai_input == 2 ) or (user_input == 2 and ai_input == 0 ) or (user_input == 3 and ai_input == 1):
         print('对方出的是%s,%s'%(_translate(ai_input),WIN_INFO))
    elif (user_input - 1 ) == ai_input:
        print('对方出的是%s,%s'%(_translate(ai_input),DOGFALL_INFO))
    else:
        print('对方出的是%s,%s'%(_translate(ai_input),LOSE_INFO))
