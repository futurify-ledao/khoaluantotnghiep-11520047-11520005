from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.http import Request, Response
from spiders.testSelenium import RunnerSpider

import paramiko
import threading
import scrapydo
import json
import io, json

import shutil

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/my-link/')
def my_link():
  scrapydo.setup()
  my_crawl()
  return render_template('abc.html')

def my_crawl():  
  items = scrapydo.run_spider(RunnerSpider)
  
  text_file = open("tmp.json", "w")
  text_file.write("%s" % items)
  text_file.close()
  
  f1 = open('tmp.json', 'r')
  f2 = open('tmp_result.json', 'w')
  for line in f1:
    f2.write(line.replace("'", '"'))
  f1.close()
  f2.close()

  f3 = open('tmp_result.json', 'r')
  f4 = open('result.json', 'w')
  for line in f3:
    f4.write(line.replace('u"', '"'))
  f3.close()
  f4.close()



  #threading.Timer(5, my_crawl).start()

if __name__ == '__main__':
  app.run(debug=True)
