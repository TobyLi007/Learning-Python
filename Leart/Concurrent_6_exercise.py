import pickle
import zlib

from enum import Enum, unique
#This module implements a common interface to many different secure hash and message digest algorithms.
from hashlib import sha1 
from random import random
from threading import Thread, current_tread, local
from time import sleep
from urllib.parse import urlparse

import pymongo
import redis
import requests
from bs4 import BeautifulSoup
from bson import Binary

@unique
class SpiderStatus(Enum):
    IDLE = 0
    WORKING = 1


def decode_page(page_bytes, charsets = ('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
    return page_html


class Retry(object):
    def __init__(self, *, retry_times = 3,
                     wait_secs = 5, errors = (Exception,)):
        self.retry_times = retry_times
        self.wait_secs = wait_secs
        self.errors = errors
    def __call__(self,fn): #decorator
        def wrapper(*args,**kwargs):
            for _ in range(self.retry_times):
                try:
                    return fn(*arg, **kwargs)
                except self.errors as e:
                    print(e)
                    sleep((random()+1) * self.wait_secs)
            return None
        return wrapper

class Spider(object):
    def __init__(self):
        self.status = SpiderStatus.IDLE

        #use request.get the body from target url
        @Retry()
        def fetch(self, current_url, *, charsets = ('utf-8',),
                  user_agent = None, proxies = None):
            thread_name = current_thread().name
            print(f'[{thread_name}]: {current_url}')
            headers = {'user-agent': user_agent} if user_agent else {} #dic
            resp = requests.get(current_url, 
                                headers = headers, proxies = proxies)
            return decode_page(resp.content, charsets) \
                if resp.status_code == 200 else None
            #It's a HTTP status code, it means "OK" (EG: The server successfully answered the http request).

        #parse the body of url by beautifulsoup lxml
        def parse(self, html_page, *, domain = 'm.sohu.com'):
            soup = BeautifulSoup(html_page, 'lxml')
            #find all a[href] in body section
            for a_tag in soup.body.select('a[href]'):
                #(Hypertext REFerence) The HTML code used to create a link to another page.
                #The HREF is an attribute of the anchor tag, which is also used to identify sections within a document. 
                parser =  urlparse(a_tag.attrs['href'])
                #URLPARSE :Parse URLs into components
                scheme = parser.scheme or 'http'
                netloc = parser.netloc or domain
                if scheme != 'javascript' and netloc == domain:
                    path = parser.path
                    query = '?' + parser.query if parser.query else ''
                    #ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                    #params='', query='', fragment='')
                    full_url = f'{scheme}://{netloc}{path}{query}'
                    redis_client = thread_local.redis_client
                    if not redis_client.sismember('visited_urls', full_url):
                        redis_client.rpush('m_sohu_task', full_url)


        def extract (self, html_page):
            pass
        def store(self, data_dict):
            #redis_client = thread_local.redis_client
            #mongo_db = thread_local.mongo_db
            pass

class SpiderThread(Thread):
    def __init__(self, name, spider):
        super().__init__(name = name, daemon = True)
        self.spider = spider

    def run(self):
        redis_client = redis.Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
        mongo_client = pymongo.MongoClient(host='1.2.3.4', port=27017)
        thread_local.redis_client = redis_client
        thread_local.mongo_db = mongo_client.msohu 
        while True:
            #Removes and returns the first element of the list stored at key.
            current_url = redis_client.lpop('m_sohu_task')
            #find the url
            while not current_url:
                current_url = redis_client.lpop('m_sohu_task')
            self.spider.status = SpiderStatus.WORKING


            current_url = current_url.decode('utf-8')
            #Returns if member is a member of the set stored at key.
            if not redis_client.sismember('visited_urls', current_url):
                redis_client.sadd('visited_urls', current_url)

                #use request.get the body from target url, returned a decoded page
                html_page = self.spider.fetch(current_url)
                if html_page not in [None, '']:
                    hasher = hasher_proto.copy()
                    #encode with SHA1
                    hasher.update(current_url.encode('utf-8'))
                    #Like digest() except the digest is returned as a string of double length, 
                    #containing only hexadecimal digits. 
                    #This may be used to exchange the value safely in email or other non-binary environments
                    doc.id = hasher.hexdigest()
                    sohu_data_coll = mongo_client.msohu.webpages
                    if not sohu_data_coll.find_one ({'_id': doc_id}):
                        sohu_data_coll.insert_one(
                            {
                                '_id': doc_id,
                                'url': current_url,
                                'page': Binary(zlib.compress(pickle.dumps(html_page)))
                                }
                            )
                        self.spider.parse(html_page)
            self.spider.status = SpiderStatus.IDLE


def is_any_live(spider_threads):
    return any(
        [spider_thread.spider.status == SpiderStatus.WORKING
                for spider_thread in spider_threads]
        )
#Constructors 
thread_local = local()
hasher_proto = sha1()

def main():
    redis_client = redis.Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
    # "Returns the number of ``names`` that exist"
    if not redis_client.exists('m_sohu_task'):
        # Insert all the specified values at the tail of the list stored at key.
        redis_client.rpush('m_sohu_task', 'http://m.sohu.com/')
    #start concurrent threads
    spider_threads = [SpiderThread('thread-%d' % i, Spider())
                      for i in range(10)]
    for spider_thread in spider_threads:
        spider_thread.start()

    while redis_client.exists('m_sohu_task') or is_any_alive(spider_threads):
        sleep(5)

    print('Over!')


if __name__ == '__main__':
    main()