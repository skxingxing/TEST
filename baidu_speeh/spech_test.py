from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17419111'
API_KEY = 'gTTNt1IfX1TAcocaymKmT4C3'
SECRET_KEY = '8KFbueFidFxYVF9Yw0foXKQ68GSWhzib'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('吕瑞芳，起床啦', 'zh', 1, {
    'vol': 5
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
