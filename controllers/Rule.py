#coding:utf-8
import tornado.web
import tornado.ioloop
import re
import sys

reload(sys)
sys.setdefaultencoding("utf8")

info = []

class Rule(tornado.web.RequestHandler):
        def get(self):
		a,b=[],[]
		try:
			a = self.request.arguments["engine"]
		except Exception,ex:
			print Exception,ex	
		try:
			b = self.request.arguments["key_status"]
		except Exception,ex:
                        print Exception,ex
		print a,b
		self.render('rule.html',title='rule',items=info)


        def post(self):
		info = ['a','b','c']
		self.render('rule.html',title='rule',items=info)
