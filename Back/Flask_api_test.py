# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, request
import requests
import random

app = Flask(__name__)

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

@app.route('/json')
def json() :
	return '{"helloWorld":"hello"}'

@app.route('/red')
def red() :
    F = request.args.get('go')
    return redirect(F)
