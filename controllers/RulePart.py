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
#		MySQL.MysqlQuery().query_update('truncate DB_REVIEW_CONTROL.tb_table_rule')
		for r in ruleDict:
			MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_table_rule(rule_name,variable,variable_rule,create_date,update_date) values("%s","%s","%s",now(),now()) ' %(ruleName,r,ruleDict[r]))


	def getRules(self):
		rules = MySQL.MysqlQuery().query_select('select distinct(rule_name) from DB_REVIEW_CONTROL.tb_table_rule ')
		#print rules
		ruleList = []
		for rule in rules:
			ruleList.append(rule[0])
		return ruleList
		#return rules

if __name__ == "__main__":
	t = RulePart()
	tb_dict = dict((['engine','InnoDB'],['collation','utf8_general_ci'],['com_status','1'],['key_status','1'],['key_type','1']))
	rulenames =  t.getRules()
	print rulenames
