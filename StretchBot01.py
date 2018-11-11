'''
이 파이썬 파일은 봇 기능에 대한 코드
'''
import telegram

StretchBot_token = '742036806:AAHWTXuNqUIiQjY7S26jFE19ajY9OBSGujE'
Stretch = telegram.Bot(token = StretchBot_token)
updates = Stretch.getUpdates()
for u in updates:
    print(u.message)
'''
 Stretch ID = 412807955

import sys
import StretchBotModel01

def proc_start(bot, update):
    Stretch.sendMessage('스트레칭을 시작합니다')
    sound = firecracker()
    Stretch.sendMessage(sound)


def proc_rolling(bot, update):
    Stretch.sendMessage('이썁..')
    sound = firecracker()
    Stretch.sendMessage(sound)

def proc_stop(bot, update):
    Stretch.sendMessage('Stop')
    Stretch.stop()

def firecracker():
    return '팡팡!'

Stretch = StretchBotModel01.StretchBot()
# 봇 객체 선언
Stretch.add_handler('rolling', proc_rolling)
# 명령어 rolling이 입력되면,proc_rolling 함수가 실행됨

Stretch.add_handler('stop', proc_stop)
# 명령어 rolling이 입력되면,proc_rolling 함수가 실행됨

Stretch.add_handler('start', proc_start)
# 명령어 rolling이 입력되면,proc_rolling 함수가 실행됨

Stretch.start()
'''
