# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       Ntears
   date：          2018/8/17
-------------------------------------------------
   Change Activity:
                   2018/8/17:
-------------------------------------------------
"""
__author__ = 'Ntears'

import requests
import threading
import time
import random
import sys
import re
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8') 

config = {"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）",
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) ",
            "Googlebot/2.1 (+http://www.googlebot.com/bot.html) ",
            "Googlebot/2.1 (+http://www.google.com/bot.html) ",
            "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html”) ",
            "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp”) ",
            "iaskspider/2.0(+http://iask.com/help/help_index.html”) ",
            "Mozilla/5.0 (compatible; iaskspider/1.0; MSIE 6.0) ",
            "Sogou web spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07″) ",
            "Sogou Push Spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07″) ",
            "Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/”; ) ",
            "msnbot/1.0 (+http://search.msn.com/msnbot.htm”)",
            "Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) ",
            "AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3 ",
            "(compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.3 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.2.1000 Chrome/39.0.2146.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.277.400 QQBrowser/9.4.7658.400",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.12150.8 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7"}



def getip_address(url):
	headers = {"user-agent": random.choice(list(config))}
	req = requests.get("http://ip.soshoulu.com/ajax/shoulu.ashx?_type=ipsearch&ip="+str(url),headers=headers)
	print str(req.text).split('$')[0].encode(encoding='GBK',errors='strict')+"\t"+url
  	
def show():

 	print "Usage test.py  d://ip.txt threadnum  OR ip   "


if __name__=="__main__":
	
	if len(sys.argv)<2:
		show()
		sys.exit(0)

	try:
			if re.match(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$",str(sys.argv[1])):
				getip_address(sys.argv[1])
			else:
				f = open(sys.argv[1])
				pool = ThreadPool(processes=int(sys.argv[2]))
				results = pool.map(getip_address, f.readlines())
				pool.close()
				pool.join()
	except IOError,e:
		print "ip文件路径不正确重新输入".encode(encoding='GBK',errors='strict')
	
	
