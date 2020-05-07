from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl

from pymysql import Error

def decode_page(page_bytes, charsets = ('utf=8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
    return page_html

def get_page_html(seed_url, *, retry_times = 3,  charsets = ('utf=8',)):
    page_html = None
    try:
        # 请求获取HTML
        page_html =decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        if retry_times>0:
            return get_page_html(seed_url, retry_times=retry_times - 1,charsets=charsets)
    return page_html
def get_matched_parts(page_html,pattern_str, pattern_ignore_case = re.I):
    """findall() returns a list of matching strings:"""
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []

def start_crawl(seed_url, match_pattern,*,max_depth = -1):
    #link to SQL server with database name 'crawler'
    conn = pymysql.connect(host = 'localhost', port = 3306,
                           database = 'crawler', user = 'root',
                           password = '7758', charset = 'utf8mb4')
    try:
        with conn.cursor() as cursor:
            # 通过下面的字典避免重复抓取并控制抓取深度
            # seed_url pass to dictionary table visited_url_list
            url_list = [seed_url]
            visited_url_list = {seed_url: 0}
            #loop for all url_list values
            while url_list:
                #pop the first value from url_list
                current_url = url_list.pop(0)
                #manage depth and get rid of duplicates
                depth = visited_url_list[current_url]
                 # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
                if depth != max_depth:
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in visited_url_list:
                            #depth management
                            visited_url_list[link] = depth +1

                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html, r'(?<= target="_blank>)\w+(?= </a></span>)')
                            if headings:
                                param_list.append((headings[0], link))
                    #SQL communication
                    cursor.executemany('insert into tb_result (heading, links) values (%s, %s)',
                                       param_list)
                    conn.commit()
    except Error:
        pass
    finally:
        conn.close()
def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'(?<=\bhref=").+(?=" target="_blank">)',
                max_depth=2)
if __name__ == '__main__':
    main()