import requests
import json
import random
from hashlib import md5

def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def getRandomSet(bits):#Ouputs random string
    num_set = [chr(i) for i in range(48,58)]
    value_set = "".join(random.sample(num_set, bits))
    return value_set

def sign_generate(tar,salt):
    tmp = "20220328001145404"+tar+salt+"QsEl4tyvTTnxX4vzhyNf"
    tmp = md5(tmp.encode(encoding='UTF-8')).hexdigest()
    return tmp

tar= "convolution"
Headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
}

def getDict(tar, origin_lng = 'en', target_lng = 'zh'):
    if isChinese(tar) == True:
        origin_lng = 'zh'
        target_lng = 'en'
    salt = str(getRandomSet(10))
    sgn = sign_generate(tar, salt)
    Url = "https://fanyi-api.baidu.com/api/trans/vip/translate?q=" + tar + "&from=" + origin_lng + "&to=" + target_lng + "&appid=20220328001145404&salt=" + salt + "&sign=" + sgn
    session = requests.Session()
    session.trust_env = False
    rtn = session.get(url = Url,
                       headers = Headers,)
    rtn = rtn.text
    rtn = json.loads(rtn)
    rtn = rtn['trans_result']
    rtn = rtn[0]
    rtn = rtn['dst']
    return rtn