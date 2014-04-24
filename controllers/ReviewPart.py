#coding:utf-8
import sys
import os.path
import tornado.web
import tornado.ioloop
import os
import re
import ConfigParser
import MySQL
import RulePart

reload(sys)
sys.setdefaultencoding("utf8")

class ReviewPart():


        def review_table(self,db,tb):
                # Table Rules
		tableRules = RulePart.RulePart().getRulesTails()
		#print  tableRules

                tb_info = MySQL.MysqlQuery().query_select('select * from information_schema.TABLES where table_schema="%s" and table_name="%s" ' %(db,tb))
                tb_key_info = MySQL.MysqlQuery().query_select('select * from  information_schema.KEY_COLUMN_USAGE where table_schema="%s" and table_name="%s" limit 1' %(db,tb))

		if tableRules['key_status'] != '1' or (tb_key_info and tb_key_info[0][2] == "PRIMARY"):
			pass
                else:
                        result = "缺少主键"
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s")' %(tb,result))
                if tb_info[0][4]  in tableRules['engine']:
                        pass;
                else:
                        result =  "存储引擎错误，只支持 %s" %(tableRules['engine'])
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
#                charset = re.match(r'utf8',tb_info[0][17])
                if tb_info[0][17] in tableRules['collation']:
                        pass;
                else:
                        result = "字符编码错误，只支持 %s" %(tableRules['charset'])
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                if tb_info[0][17] in tableRules['collation']:
                        pass;
                else:
                        result = "字符校验错误，只支持 %s" %(tableRules['collation'])
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                if tb_info[0][19] == "":
                        pass;
                else:
                        result =  "禁止添加非必要参数 %s" %(tb,tb_info[0][19])
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                if tb_info[0][20] != "":
                        pass;
	        if tb_info[0][20] == "" and tableRules['com_status'] == '1':
  	      		result =  "请给表 %s 添加上Comment注释信息" %(tb)
               		MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                else:
			pass
  	      		#result =  "请给表 %s 添加上Comment注释信息" %(tb)
               		#MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
#                tb_key_info = MySQL.MysqlQuery().query_select('select * from  information_schema.KEY_COLUMN_USAGE where table_schema="%s" and table_name="%s" limit 1' %(db,tb))
#                if tb_key_info:
#                         if  tb_key_info[0][2] == "PRIMARY":
#                                pass;
#                else:
#                        result = "表 %s 没有主键，请添加" %(tb)
#                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s")' %(tb,result))
#                if tb_info[0][4] == "InnoDB":
#                        pass;
#                else:
#                        result =  "请将表 %s 的存储引擎设为 InnoDB" %(tb)
#                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
#                charset = re.match(r'utf8',tb_info[0][17])
#                if charset:
#                        pass;
#                else:
#                        result = "请将表 %s 的字符编码设为 utf-8" %(tb)
#                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
#                if tb_info[0][19] == "":
#                        pass;
#                else:
#                        result =  "请不要为表 %s 添加非必要参数 %s" %(tb,tb_info[0][19])
#                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
#	        if tb_info[0][20] != "":
#          	         pass;
#                else:
#  	      		result =  "请给表 %s 添加上Comment注释信息" %(tb)
#               		MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))

        def review_column(self,db,tb):
                tb_col = MySQL.MysqlQuery().query_select('select * from information_schema.COLUMNS where table_schema="%s" and table_name="%s" ' %(db,tb))
                for col_info in tb_col:
                        if col_info[3] == 'id' or col_info[3] == 'ID' or col_info[18] != '':
                                pass;
                        else:
                                result =  "缺少comment注释"
                                MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,tb_col,result) values("%s","%s","%s") ' %(tb,col_info[3],result))
                        if col_info[15] == 'PRI':
                                if col_info[7] == 'int' and  col_info[16] == 'auto_increment':
                                        pass;
                                else:
                                        result =  "主键字段类型错误， 必须是INT型，且必须是自增的"
                                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
        def review_index():
                pass;

	
	def review_extra(self,db,tb):
		col_ex = []
		tb_col = MySQL.MysqlQuery().query_select('select * from information_schema.COLUMNS where table_schema="%s" and table_name="%s" ' %(db,tb))
		for col_info in tb_col:
			col_ex.append(col_info[3].lower())
		update_st = set(col_ex)-set(['update','update_date','update_time','updatedate','updatetime'])
		create_st = set(col_ex)-set(['create','create_date','create_time','createdate','createtime'])
		if len(tb_col) > len(list(update_st)):
			key_col = set(col_ex) - update_st
			for i in tb_col:
				#print i[3].lower(),list(key_col)[0]
				if i[3].lower() != list(key_col)[0]:
					pass
				elif  i[5] == 'CURRENT_TIMESTAMP' and (i[7] == 'timestamp' or i[7] == 'datetime' ) and i[16] == 'on update CURRENT_TIMESTAMP':
					pass
		#			print "have update"
				else:
					result = "字段类型或默认值错误，eg:`update_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'"
					MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,tb_col,result) values("%s","%s","%s") ' %(tb,i[3],result))
		else:
			result = "不存在update类记录表数据修改时间的字段"
			MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
		#if 'update_date' in  col_ex:
		#	print "have update"
		#else:
	#		pass
		if len(tb_col) > len(list(create_st)):
			pass;
                #                       MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,tb_col,result) values("%s","%s","%s") ' %(tb,i[3],result))
                else:
                        result = "不存在create类记录表创建时间的字段，"
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))

#if __name__ == "__main__":
#	t = ReviewPart()
#	t.review_extra('DB_REVIEW','audit_data4')
