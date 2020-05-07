import pickle
import zlib

from enum import Enum, unique
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

        @Retry()
        def fetch(self, current_url, *, charsets = ('utf-8',),
                  user_agent = None, proxies = None):
            thread_name = current_thread().name
            print(f'[{thread_name}]: {current_url}')
            headers = {'user-agent': user_agent} if user_agent else {}
