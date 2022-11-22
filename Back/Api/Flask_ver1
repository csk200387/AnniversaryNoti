# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, request
import requests, random, json
from datetime import datetime
from pytz import timezone

app = Flask(__name__)
directory = "/home/saradan/mysite/anniData.json"
errorMessage = """{
	"code": "BAD",
	"message": "해당하는 날짜의 기념일 없음"
}"""

# 외국 서버이므로 한국 시간으로 설정
KST = timezone('Etc/GMT-9')

# json load
f = open(directory, "r", encoding="utf-8")
anni_json = json.load(f)
f.close()




# flask page
@app.route('/')
def ran() :
    dic = {}
    for i in range(1,10):
        a = random.randrange(1,10**i)
        b = random.randrange(10**(i-1),10**i)
        c = random.randrange(10**(i-1),10**i)
        d = random.randrange(10**(i-1),10**i)
        e = random.randrange(10**(i-1),10**i)
        f = random.randrange(10**(i-1),10**i)
        dic['luckyNum'+str(i)] = [a,b,c,d,e,f]
    return dic

@app.route('/hello')
def hello() :
    return random.choice(['<body bgcolor="blue">Hi this page is hello</body>', '<body bgcolor="green">Hi this page is hello</body>', '<body bgcolor="red">Hi this page is hello</body>'])

@app.route('/annijson')
def annijson() :
    data = json.dumps(anni_json, ensure_ascii=False)
    return data

@app.route('/api')
def api() :
    try :
        mon = request.args.get("m")
        dat = request.args.get("d")
        res = f"{mon}월 {dat}일"
        a = json.dumps({res:anni_json[res]}, ensure_ascii=False)
        return a
    except :
        return errorMessage

@app.route('/red')
def red() :
    F = request.args.get('go')
    return redirect(F)
