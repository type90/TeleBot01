'''
이 파이썬 파일은 봇 기능에 대한 코드
import telegram

StretchBot_token = '742036806:AAHWTXuNqUIiQjY7S26jFE19ajY9OBSGujE'
Stretch = telegram.Bot(token = StretchBot_token)
updates = Stretch.getUpdates()
for u in updates:
    print(u.message)

 Stretch ID = 412807955
'''
print('개발환경 설정')
import sys
import StretchBotModel01

def proc_start(bot, update):
    chii.sendMessage('스트레칭을 시작합니다')
    sound = firecracker()
    chii.sendMessage(sound)


def proc_rolling(bot, update):
    chii.sendMessage('데구르르..')
    sound = firecracker()
    chii.sendMessage(sound)
    chii.sendMessage('르르..')

def proc_stop(bot, update):
    chii.sendMessage('Stop')
    chii.stop()

def firecracker():
    return '팡팡!'

chii = StretchBotModel01.StretchBot()
# 봇 객체 선언
chii.add_handler('rolling', proc_rolling)
# 명령어 rolling이 입력되면,proc_rolling 함수가 실행됨

chii.add_handler('stop', proc_stop)
# 명령어 rolling이 입력되면,proc_rolling 함수가 실행됨

chii.add_handler('start', proc_start)
# 명령어 rolling이 입력되면,proc_rolling 함수가 실행됨

chii.start()
