'''
import telegram
from telegram.ext import Updater, CommandHandler
'''
'''
이 파이썬 파일은 봇 관리
 - 토큰관리
 - 초기화 함수
 - sendMessage : 메세지 보내는 함수BotChii
 - stop : 종료 함수
 - add_handler : 기능 추가

'''
'''

class TelegramBot:
    
    #초기 설정
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 412807955
        # id = 사용자의 Id (Tate.kim)

    #메세지 보내기 함수
    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    #종료 함수
    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.sendMessage('웜업을 종료합니다')
        self.updater.stop()

class StretchBot(TelegramBot):
    def __init__(self):
        self.token = '742036806:AAHWTXuNqUIiQjY7S26jFE19ajY9OBSGujE'
        TelegramBot.__init__(self, '412807955', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('스트레칭봇을 시작합니다')
        self.updater.start_polling()
        self.updater.idle()

'''