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
		tabelRules = RulePart.RulePart().getRulesTails()
                tb_info = MySQL.MysqlQuery().query_select('select * from information_schema.TABLES where table_schema="%s" and table_name="%s" ' %(db,tb))
                tb_key_info = MySQL.MysqlQuery().query_select('select * from  information_schema.KEY_COLUMN_USAGE where table_schema="%s" and table_name="%s" limit 1' %(db,tb))
                if tb_key_info:
                         if  tb_key_info[0][2] == "PRIMARY":
                                pass;
                else:
                        result = "表 %s 没有主键，请添加" %(tb)
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s")' %(tb,result))
                if tb_info[0][4] == "InnoDB":
                        pass;
                else:
                        result =  "请将表 %s 的存储引擎设为 InnoDB" %(tb)
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                charset = re.match(r'utf8',tb_info[0][17])
                if charset:
                        pass;
                else:
                        result = "请将表 %s 的字符编码设为 utf-8" %(tb)
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                if tb_info[0][19] == "":
                        pass;
                else:
                        result =  "请不要为表 %s 添加非必要参数 %s" %(tb,tb_info[0][19])
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                if tb_info[0][20] != "":
                        pass;
#                tb_key_info = MySQL.MysqlQuery().query_select('select * from  information_schema.KEY_COLUMN_USAGE where table_schema="%s" and table_name="%s" limit 1' %(db,tb))
#                if tb_key_info:
#                         if  tb_key_info[0][2] == "PRIMARY":
#                                pass;
#                else:
#                        result = "表 %s 没有主键，请添加" %(tb)
#                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s")' %(tb,result))
                if tb_info[0][4] == "InnoDB":
                        pass;
                else:
                        result =  "请将表 %s 的存储引擎设为 InnoDB" %(tb)
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                charset = re.match(r'utf8',tb_info[0][17])
                if charset:
                        pass;
                else:
                        result = "请将表 %s 的字符编码设为 utf-8" %(tb)
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                if tb_info[0][19] == "":
                        pass;
                else:
                        result =  "请不要为表 %s 添加非必要参数 %s" %(tb,tb_info[0][19])
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                if tb_info[0][20] != "":
                        pass;
                else:
                        result =  "请给表 %s 添加上Comment注释信息" %(tb)
                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))

        def review_column(self,db,tb):
                tb_col = MySQL.MysqlQuery().query_select('select * from information_schema.COLUMNS where table_schema="%s" and table_name="%s" ' %(db,tb))
                for col_info in tb_col:
                        if col_info[18] != '':
                                pass;
                        else:
                                result =  "请为表 %s 字段 %s 添加comment注释" %(tb,col_info[3])
                                MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
                        if col_info[15] == 'PRI':
                                if col_info[7] == 'int' and  col_info[16] == 'auto_increment':
                                        pass;
                                else:
                                        result =  "表 %s 主键 %s必须是INT型，且必须是自增的" %(tb,col_info[3])
                                        MySQL.MysqlQuery().query_update('insert into DB_REVIEW_CONTROL.tb_review_result(tb_name,result) values("%s","%s") ' %(tb,result))
        def review_index():
                pass;

