# -*- coding: utf-8 -*-
'''图灵'''
import sys
import os
import requests
import json
import urllib2
import demjson
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import bsidu_stt
from tts import baidu_tts
import snowboy
import speaker
import recorder

def start(text):
  
    main(text)
    
def main(text):
    
    ak = 'c380ed8f2880443c84892ace36ba6bad'
    ui = '167031'
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
	              "reqType":0,
                "perception": {
                    "inputText": {
                        "text": text
                    },
                },
                "userInfo": {
                    "apiKey": ak,
                    "userId": ui
                }
    }

    talkback = requests.post(url, data=data)
    talkback_data = demjson.decode(talkback)
    print talkback_data
    saytext = talkback_data['results']['values']['text']

    bt = baidu_tts()
    tok = bt.get_token()
    bt.tts(saytext, tok)
    speaker.speak()
    
