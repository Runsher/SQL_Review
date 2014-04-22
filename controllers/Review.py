#coding:utf-8
import sys
import os.path
import tornado.web
import tornado.ioloop
import os
import re
import ConfigParser
import MySQL
import ReviewPart

reload(sys)
sys.setdefaultencoding("utf8")

info = []
review_status = 0

class LoadAndClean():
	def find_Load(self):
		for file in os.listdir("tmp/"):
          		self.SqlTextIn="tmp/"+file
            		MySQL.MysqlLoad().loadin(self.SqlTextIn)

	def del_tmp_file(self,tb):
		for file in os.listdir("tmp"):
			if file:
				SqlTextIn="tmp/"+file
				os.remove(SqlTextIn)
			else:
				pass
		tb_d = ['DB_REVIEW',"%s" %(tb)]
		tb_del = '.'.join(tb_d)
		tb_b = ['DB_REVIEW_BAK',"%s" %(tb)]
		tb_bak = '.'.join(tb_b)
		MySQL.MysqlQuery().query_update('drop table if exists %s' %(tb_bak))
		MySQL.MysqlQuery().query_update('rename table %s to %s' %(tb_del,tb_bak)) 
		#MySQL.MysqlQuery().query_update('drop table if exists %s' %(tb_del)) 



class Review(tornado.web.RequestHandler):
	def get(self):
		self.render('review.html',title='result_test',items=info,status=review_status)


	def post(self):
		review_status_info = 0
                upload_path = os.path.join(os.path.dirname(__file__),'../tmp')  
		info = []
		try:
                	file_metas = self.request.files['file']   
		except Exception,ex:
			print Exception,ex
			if self.get_argument('content'):
				file_me = self.get_argument('content')
				f = open(upload_path+'/'+'tmp_file','w')
				f.write(file_me)
				f.close()
                                LoadAndClean().find_Load()
                                max_id = MySQL.MysqlQuery().query_select('select max(id) from DB_REVIEW_CONTROL.tb_review_result')[0][0]
                                tb_name = MySQL.MysqlQuery().query_select('show tables from %s' %(MySQL.db))
                                if tb_name:
                                        for tb_tup in tb_name:
                                                tb = "".join(tuple(tb_tup))
                                                ReviewPart.ReviewPart().review_table(MySQL.db,tb)
                                                ReviewPart.ReviewPart().review_column(MySQL.db,tb)
						ReviewPart.ReviewPart().review_extra(MySQL.db,tb)
                                        rs_info = MySQL.MysqlQuery().query_select('select tb_name,tb_col,result from DB_REVIEW_CONTROL.tb_review_result where id > %s' %(max_id))
                                        if rs_info:
						review_status = 2
	                                    	info = rs_info
                                                #for rs in rs_info:
                                                 #       info.append(rs[0])
                                        else:
						review_status = 1
                                else:
					review_status = 3
			else:
				review_status = 4
                      	try:
                          	for tb_del in tb_name:
                                   	LoadAndClean().del_tmp_file(tb_del[0])
                      	except Exception,ex:
				print Exception,ex
		else:
                	for meta in file_metas:
                        	filename = meta['filename']
                        	filepath = os.path.join(upload_path,filename)
                        	with open(filepath,'wb') as up:      
                               		up.write(meta['body'])
				LoadAndClean().find_Load()
				max_id = MySQL.MysqlQuery().query_select('select max(id) from DB_REVIEW_CONTROL.tb_review_result')[0][0]
				tb_name = MySQL.MysqlQuery().query_select('show tables from %s' %(MySQL.db))
				if tb_name:
					for tb_tup in tb_name:
						tb = "".join(tuple(tb_tup))
						ReviewPart.ReviewPart().review_table(MySQL.db,tb)
						ReviewPart.ReviewPart().review_column(MySQL.db,tb)	
						ReviewPart.ReviewPart().review_extra(MySQL.db,tb)	
					rs_info = MySQL.MysqlQuery().query_select('select tb_name,tb_col,result from DB_REVIEW_CONTROL.tb_review_result where id > %s' %(max_id))
					if rs_info:
						review_status = 2
						info = rs_info
					else:
						review_status = 1
				else:
					review_status = 3
		#	else:   
		#		review_status = 4 
			try:
				for tb_del in tb_name:
					LoadAndClean().del_tmp_file(tb_del[0])
			except Exception,ex:
                       		print Exception,ex
		self.render('review.html',title='result_test',items=info,status=review_status)
		info = []
		
