from flask_cors import CORS, cross_origin
import csv
from bs4 import BeautifulSoup
import random
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import selenium as sn
from selenium.webdriver.common.proxy import *
import requests
from flask import Flask,jsonify

proxies = ['http://vaibhav:vaibhav@191.102.154.23:12345','http://vaibhav:vaibhav@46.29.248.102:12345','http://vaibhav:vaibhav@23.104.184.58:12345','http://vaibhav:vaibhav@107.158.86.114:12345','http://vaibhav:vaibhav@107.158.86.125:12345','http://vaibhav:vaibhav@23.104.184.36:12345','http://vaibhav:vaibhav@191.102.154.7:12345','http://vaibhav:vaibhav@191.102.154.254:12345','http://vaibhav:vaibhav@107.158.25.129:12345','http://vaibhav:vaibhav@23.104.184.216:12345','http://vaibhav:vaibhav@23.104.184.65:12345','http://vaibhav:vaibhav@200.10.41.152:12345','http://vaibhav:vaibhav@200.10.41.30:12345','http://vaibhav:vaibhav@107.158.86.111:12345','http://vaibhav:vaibhav@200.10.41.81:12345','http://vaibhav:vaibhav@107.158.25.144:12345','http://vaibhav:vaibhav@107.158.86.161:12345','http://vaibhav:vaibhav@107.158.25.121:12345','http://vaibhav:vaibhav@46.29.248.100:12345','http://vaibhav:vaibhav@200.10.41.114:12345',
           'http://vaibhav:vaibhav@155.94.171.73:12345','http://vaibhav:vaibhav@46.29.250.125:12345','http://vaibhav:vaibhav@191.101.118.152:12345','http://vaibhav:vaibhav@165.231.212.163:12345','http://vaibhav:vaibhav@5.157.0.165:12345','http://vaibhav:vaibhav@191.101.118.11:12345','http://vaibhav:vaibhav@173.254.247.19:12345','http://vaibhav:vaibhav@155.94.171.78:12345','http://vaibhav:vaibhav@191.101.118.231:12345','http://vaibhav:vaibhav@91.108.178.117:12345'] 
HEADERS = [{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
            'Accept-Language': 'en-US, en;q=0.5'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept-Language': 'en-US, en;q=0.5'}]
app = Flask(__name__)
CORS(app)

@app.route("/you_tube/<keyword>", methods = ["GET"])

def get_questions(keyword):
    try:
        head = random.choices(HEADERS)[0]["User-Agent"]
        opts = Options()
        myproxy = random.choices(proxies)
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': myproxy,
            'ftpProxy': myproxy,
            'sslProxy': myproxy,
            'noProxy': '',
            })
        opts.add_argument("user-agent="+head)
        opts.proxy = proxy
        driver = webdriver.Chrome("chromedriver.exe",options=opts) ## add the chromedriver path
        URL = "https://www.youtube.com/results?search_query="+keyword
        driver.get(URL)
        parse = BeautifulSoup(driver.page_source, "html.parser")
        title = parse.find_all("a" , attrs = {"id":"video-title"})[0]
        return("https://www.youtube.com/"+title["href"])
    except Exception as e:
        print(e)
        return("Error")

if __name__ == "__main__":
    app.run(debug=True)
