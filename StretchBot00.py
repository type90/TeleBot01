'''
파일 설명 :
테스트용 계정 : ConnectTestBot01
1. 최초에 챗봇을 생성하고, 지정된 토큰값으로 맞게 통신됨을 확인하는 용도
2. 텔레그램의 대화내용이 어떻게 저장되는지를 보여줌.

'''

import telegram

chatbot_token = '707605708:AAGl0UnnW9jnF8X8g5YpvFcl60fFFW22xq4'
chatbot = telegram.Bot(token = chatbot_token)
updates = chatbot .getUpdates()
for u in updates:
    print(u.message)

'''
u(메세지)가 JSON 비슷한 형태로 출력되는 것을 볼 수 있다.

이것은 SOA구조라고 하던데 좀 더 공부가 필요할듯!
{'message_id': 1, 'date': 1541949359, 'chat': {'id': 412807955, 'type': 'private', 'username': 'tatekim', 'first_name': 'Tate', 'last_name': 'Kim'},'text': '/start', 'entities': [{'type': 'bot_command', 'offset': 0, 'length': 6}], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 412807955, 'first_name': 'Tate', 'is_bot': False, 'last_name': 'Kim', 'username': 'tatekim', 'language_code': 'ko-KR'}}
1541949359 시간에 tatekim 유저가 1번째 메세지로 /start 라는 텍스트 메세지를 보냈다.
{'message_id': 2, 'date': 1541949595, 'chat': {'id': 412807955, 'type': 'private', 'username': 'tatekim', 'first_name': 'Tate', 'last_name': 'Kim'}, 'text': 'hi', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 412807955, 'first_name': 'Tate', 'is_bot': False, 'last_name': 'Kim', 'username': 'tatekim', 'language_code': 'ko-KR'}}
{'message_id': 3, 'date': 1541949798, 'chat': {'id': 412807955, 'type': 'private', 'username': 'tatekim', 'first_name': 'Tate', 'last_name': 'Kim'}, 'entities': [], 'caption_entities': [], 'photo': [{'file_id': 'AgADBQADUqkxG1R-SVfSE_2YebxcRX-l1jIABHNORElRvWj0xPUDAAEC', 'width': 67, 'height': 90, 'file_size': 1202}, {'file_id': 'AgADBQADUqkxG1R-SVfSE_2YebxcRX-l1jIABJ4HZbf2iUdXxfUDAAEC', 'width': 240, 'height': 320, 'file_size': 12446}, {'file_id': 'AgADBQADUqkxG1R-SVfSE_2YebxcRX-l1jIABDy0a5y8hOLHw_UDAAEC', 'width': 600, 'height': 800, 'file_size': 50876}, {'file_id': 'AgADBQADUqkxG1R-SVfSE_2YebxcRX-l1jIABLqWLFeoP-IywvUDAAEC', 'width': 960, 'height': 1280, 'file_size': 117972}], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 412807955, 'first_name': 'Tate', 'is_bot': False, 'last_name': 'Kim', 'username': 'tatekim', 'language_code': 'ko-KR'}}
{'message_id': 4, 'date': 1541949819, 'chat': {'id': 412807955, 'type': 'private', 'username': 'tatekim', 'first_name': 'Tate', 'last_name': 'Kim'}, 'entities': [], 'caption_entities': [], 'document': {'file_id': 'BQADBQADPQADVH5JV0D4zzAZEMLDAg', 'thumb': {'file_id': 'AAQFABOTUt4yAASG2ESTNuaxhq8NAAIC', 'width': 67, 'height': 90, 'file_size': 2387}, 'file_name': '자전거셀카.jpg', 'mime_type': 'image/jpeg', 'file_size': 1503703}, 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 412807955, 'first_name': 'Tate', 'is_bot': False, 'last_name': 'Kim', 'username': 'tatekim', 'language_code': 'ko-KR'}}


웹 브라우저 상에서 확인할 수 있는 방법 :  
https://api.telegram.org/bot[토큰값]/getUpdates
https://api.telegram.org/bot707605708:AAGl0UnnW9jnF8X8g5YpvFcl60fFFW22xq4/getUpdates

웹 브라우저 상에서 Bot -> USER로 메세지를 보내보는 법  
https://api.telegram.org/bot707605708:AAGl0UnnW9jnF8X8g5YpvFcl60fFFW22xq4/sendmessage?chat_id=412807955&text=ConnectTestBot01 says hi
실제로 바로 받는 모습을 볼 수 있다.

https://core.telegram.org/bots/api
API를 제공해주기 떄문에
https://토큰값/ api명령어?채팅방_id=내용
포맷으로 다양한 방식의 메소드를 통한 제어 가능

    getMe // sendMessage
    https://api.telegram.org/bot707605708:AAGl0UnnW9jnF8X8g5YpvFcl60fFFW22xq4/sendmessage?chat_id=412807955&text=ConnectTestBot01 says <b>hi</b>
    
    sendPhoto : AgADBQADUqkxG1R-SVfSE_2YebxcRX-l1jIABHNORElRvWj0xPUDAAEC 라는 이름의 사진(텔레그램 상에 저장되어 있음)을 보내보는 메소드
    https://api.telegram.org/bot707605708:AAGl0UnnW9jnF8X8g5YpvFcl60fFFW22xq4/sendPhoto?chat_id=412807955&photo=AgADBQADUqkxG1R-SVfSE_2YebxcRX-l1jIABHNORElRvWj0xPUDAAEC
    서버에 사진을 올릴 수 있습니다!

    기타 sendAudio, sendDocument, sendVideo, sendAnimation
    
    InlineQueryResult <- 인라인 쿼리 결과를 반환합니다.
    @CAT을 쳤을때의 결과를 보면 재미있음
+


'''