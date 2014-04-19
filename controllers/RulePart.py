#coding:utf-8
import time
import datetime
import sys
import os.path
import os
import re
import MySQL

reload(sys)
sys.setdefaultencoding("utf8")

class RulePart():
	def handlerRules(self,ruleName,ruleDict):
		now = time.localtime()
		str_now = time.strftime("%Y %m %d %X", now )
		print str_now
#		MySQL.MysqlQuery().query_update('truncate DB_REVIEW_CONTROL.tb_table_rule')
		for r in ruleDict:
			MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_table_rule(rule_name,variable,variable_rule,create_date,update_date) values("%s","%s","%s","%s","%s") ' %(ruleName,r,ruleDict[r],str_now,str_now))


	def getRules(self):
		rules = MySQL.MysqlQuery().query_select('select distinct(rule_name),create_date,update_date from DB_REVIEW_CONTROL.tb_table_rule ')
		#print rules
		#ruleList = []
		#for rule in rules:
		#	ruleList.append(rule[0])
		#return ruleList
		return rules
	

	def getRulesTails(self):
		engines,collations,charset,com_status,key_status,key_type = [],[],[],[],[],[]
		engine = MySQL.MysqlQuery().query_select('select distinct(variable_rule) from DB_REVIEW_CONTROL.tb_table_rule where rule_status=1 and variable="engine"')
		#test = MySQL.MysqlQuery().query_select('select variable,variable_rule from DB_REVIEW_CONTROL.tb_table_rule where rule_status=1')
		#print test
		for i in engine:
			engines.append(i[0])

		charse = MySQL.MysqlQuery().query_select('select distinct(variable_rule) from DB_REVIEW_CONTROL.tb_table_rule where rule_status=1 and variable="charset"')
		for i in charse:
			charset.append(i[0])

		collation = MySQL.MysqlQuery().query_select('select distinct(variable_rule) from DB_REVIEW_CONTROL.tb_table_rule where rule_status=1 and variable="collation"')
		for i in collation:
			collations.append(i[0])
		
		com_statu = MySQL.MysqlQuery().query_select('select distinct(variable_rule) from DB_REVIEW_CONTROL.tb_table_rule where rule_status=1 and variable="com_status"')
		com_status = com_statu[0][0]

		key_statu = MySQL.MysqlQuery().query_select('select distinct(variable_rule) from DB_REVIEW_CONTROL.tb_table_rule where rule_status=1 and variable="key_status"')
		key_status = key_statu[0][0]

		key_typ = MySQL.MysqlQuery().query_select('select distinct(variable_rule) from DB_REVIEW_CONTROL.tb_table_rule where rule_status=1 and variable="key_type"')
		key_type = key_typ[0][0]

		ruleTailDict = dict((['engine',engines],['collation',collations],['charset',charset],['com_status',com_status],['key_status',key_status],['key_type',key_type]))
		return ruleTailDict

if __name__ == "__main__":
	t = RulePart()
#	tb_dict = dict((['engine','InnoDB'],['collation','utf8_general_ci'],['com_status','1'],['key_status','1'],['key_type','1']))
#	tb_name = 'rule2'
#	t.handlerRules(tb_name,tb_dict)
#	rulenames =  t.getRules()
#	print rulenames
	tbru = t.getRulesTails()
	print tbru
	#print tbru['engine']
	#for k,y in tbru.iteritems():
	#	if k == 'engine':
	#		print y
