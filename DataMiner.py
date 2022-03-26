import requests
import json
import random
from bs4 import BeautifulSoup

def getRandomSet(bits):#Ouputs random string
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    total_set = num_set + char_set
    value_set = "".join(random.sample(total_set, bits))
    return value_set

def getToken():#Outputs Token string
    return getRandomSet(bits = 8)+'-'+getRandomSet(bits = 4)+'-'+getRandomSet(bits = 4)+'-'+getRandomSet(bits = 4)+'-'+getRandomSet(bits = 12)

def Reqst(tar):#Post to Server
    Headers['Token'] = getToken()
    Pyload = {'words': tar}
    Pyload = json.dumps(Pyload)
    session = requests.Session()
    session.trust_env = False
    req = session.post(url=Url,
                        headers=Headers,
                        data=Pyload)
    statues_code = req.status_code
    req = req.text
    req = json.loads(req)
    return req

def ObtAcdDic(tar): #Obatain Academic Dictionary
    req = Reqst(tar)
    if (req['code'] != 200):
        print('Aborted! Access Failed | Error Code: ', req['code'])
        return None
    print(req)
    try:
        req = req['data']
        req = req['dictsVos']
        req = req[0]
        req = req['adictsVo']
        req = req['dicts']
        req = req[tar]
    except Exception as e:
        req = [{"name": "Error Obatain Dictionary Failed!"},{"name":e}]
    del Headers['Token']
    return req

def ObtProDic(tar): #Obatain Professional Dictionary
    req = Reqst(tar)
    if(req['code']!=200):
        print('Aborted! Access Failed | Error Code: ',req['code'])
        return None
    try:
        req = req['data']
        req = req['dictsVos']
        req = req[0]
        req = req['pdictsVo']
        req = req['dicts']
        req = req[tar]
    except:
        req = [{"name":"Error Obatain Dictionary Failed!"}]
    del Headers['Token']
    return req

tar= "hello"

Url = "https://dict.cnki.net/fyzs-front-api/translate/querytranslatedate"
Headers = {
    "Content-Type":"application/json;charset=UTF-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
    "Host": "dict.cnki.net",
    "Connection": "keep-alive",
    "Content-Length": "15",
    "sec-ch-ua" : "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://dict.cnki.net",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://dict.cnki.net/index",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}



ans = ObtAcdDic(tar)
#for i in ans:
#    print(i['name'],i['wordFreq'])
print(ans)

def demi_return():
    demi_dict = [
        {"name": "11111111################################################################################################","wordFreq":"88"},
        {"name": "22222222################################################################################################","wordFreq":"88"},
        {"name": "33333333################################################################################################","wordFreq":"88"},
        {"name": "44444444################################################################################################","wordFreq":"88"},
        {"name": "55555555################################################################################################","wordFreq":"88"},
        {"name": "66666666################################################################################################","wordFreq":"88"},
        {"name": "77777777################################################################################################","wordFreq":"88"},
        {"name": "88888888################################################################################################","wordFreq":"88"},
        {"name": "99999999################################################################################################","wordFreq":"88"},
        {"name": "00000000################################################################################################","wordFreq":"88"},
        {"name": "aaaaaaaa################################################################################################","wordFreq":"88"},
        {"name": "bbbbbbbb################################################################################################","wordFreq":"88"},
        {"name": "cccccccc################################################################################################","wordFreq":"88"},
        {"name": "dddddddd################################################################################################","wordFreq":"88"},
        {"name": "eeeeeeee################################################################################################","wordFreq":"88"},
        {"name": "ffffffff################################################################################################","wordFreq":"88"},
        {"name": "gggggggg################################################################################################","wordFreq":"88"},
        {"name": "hhhhhhhh################################################################################################","wordFreq":"88"},
        {"name": "iiiiiiii################################################################################################","wordFreq":"88"},
        {"name": "jjjjjjjj################################################################################################","wordFreq":"88"},
        {"name": "kkkkkkkk################################################################################################","wordFreq":"88"},
        {"name": "llllllll################################################################################################","wordFreq":"88"},
        {"name": "mmmmmmmm################################################################################################","wordFreq":"88"},
        {"name": "nnnnnnnn################################################################################################","wordFreq":"88"},
    ]
    return demi_dict

def demi1():
    d = [{'topicCode': '', 'name': 'HELLO', 'wordFreq': 9}, {'topicCode': '', 'name': '问好', 'wordFreq': 5}, {'topicCode': '', 'name': '喂', 'wordFreq': 5}, {'topicCode': '', 'name': 'HELLO协议', 'wordFreq': 5}, {'topicCode': '', 'name': '你好', 'wordFreq': 3}, {'topicCode': '', 'name': '烟芽夜蛾', 'wordFreq': 0}]
    return d