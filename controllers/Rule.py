#coding:utf-8
import tornado.web
import tornado.ioloop
import re
import sys
import RulePart

reload(sys)
sys.setdefaultencoding("utf8")

info = []
ruleList = []

class Rule(tornado.web.RequestHandler):
        def get(self):
		tb_dict = {}
		engine,collation,key_status,com_status,key_type=['None'],['None'],['0'],['0'],['0']
		try:
			engine = self.request.arguments["engine"]
		except Exception,ex:
			print Exception,ex	
		try:
			collation = self.request.arguments["collation"]
		except Exception,ex:
			print Exception,ex	
		try:
			com_status = self.request.arguments["com_status"]
		except Exception,ex:
                        print Exception,ex
		try:
			key_status = self.request.arguments["key_status"]
		except Exception,ex:
                        print Exception,ex
		try:
			key_type = self.request.arguments["key_type"]
		except Exception,ex:
                        print Exception,ex
		#print engine,collation,key_status,com_status,key_type
		try:
			tb_dict = dict((['engine',engine[0]],['collation',collation[0]],['com_status',com_status[0]],['key_status',key_status[0]],['key_type',key_type[0]]))
		except Exception,ex:
			print Exception,ex
		rule_name = 'rule'
		RulePart.RulePart().handlerRules(rule_name,tb_dict)
		ruleNames = RulePart.RulePart().getRules()
		print ruleNames
		self.render('rule.html',title='rule',items=info,ruleList=ruleNames)


        def post(self):
		pass;
#		info = ['a','b','c']
#		self.render('rule.html',title='rule',items=info)
