#-*- coding=utf-8 -*-
import random

ai_input = random.choice(range(3))
user_input = input('请输入：剪刀(0)石头(1)布(2):')
WIN_INFO = '😆\t赢了，你真的是太厉害了！'
LOSE_INFO =  '😭\t输了,不要走，洗洗手接着来，决战到天亮！'
DOGFALL_INFO = '😯\t啊哦，平局，要不再来一局？'

def _translate(_num):
    log = ['剪刀', '石头', '布']
    return log[_num]

ai_input = _translate(ai_input)

if user_input == '0':
    if ai_input == '剪刀':
        print('对方出的是%s,%s'%(ai_input,DOGFALL_INFO))
    elif ai_input == '石头':
        print('对方出的是%s,%s'%(ai_input,LOSE_INFO))
    elif ai_input == '布':
        print('对方出的是%s,%s'%(ai_input,WIN_INFO))
elif user_input == '1':
    if ai_input == '石头':
        print('对方出的是%s,%s'%(ai_input,DOGFALL_INFO))
    elif ai_input == '布':
        print('对方出的是%s,%s'%(ai_input,LOSE_INFO))
    elif ai_input == '剪刀':
        print('对方出的是%s,%s'%(ai_input,WIN_INFO))
elif user_input == '2':
    if ai_input == '布':
        print('对方出的是%s,%s'%(ai_input,DOGFALL_INFO))
    elif ai_input == '剪刀':
        print('对方出的是%s,%s'%(ai_input,LOSE_INFO))
    elif ai_input == '石头':
        print('对方出的是%s,%s'%(ai_input,WIN_INFO))
else:
    print('亲，请输入0,1,2\t 👌')
