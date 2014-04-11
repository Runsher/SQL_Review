#coding:utf8
import MySQLdb
import sys
import os
import ConfigParser
from subprocess import Popen,PIPE
import Unicode

reload(sys)
sys.setdefaultencoding("utf8")

config = ConfigParser.ConfigParser()
config.readfp(open("conf/review.conf"),"rb")

host = config.get("Global","mysql_host")
port = int(config.get("Global","mysql_port"))
user = config.get("Global","mysql_user")
passwd = config.get("Global","mysql_password")
db = config.get("Global","mysql_database")

class MysqlLoad():
        def __init__(self):
                pass;

        def loadin(self,SqlTextIn):
		Unicode.TransferToUnicode().transferToUnicode(SqlTextIn)
		process = Popen('mysql -h%s -P%s -u%s -p%s %s ' %(host,port,user,passwd,db),stdout=PIPE,stdin=PIPE,shell=True)
		process.communicate('source '+SqlTextIn)

	def loadout(self,SqlTextOut):
		pass;

class MysqlQuery():
        def __init__(self):
                pass;

        def query_select(self,sqlCommand):
		try:
                	conn = MySQLdb.connect(
                        	host = host,
                        	user = user,
                        	port = port,
                        	passwd = passwd
                	)
                	cur=conn.cursor()
                	cur.execute(sqlCommand)
                	ret = ''
                	ret = cur.fetchall()
                	return  list(ret)
                	cur.close()
			conn.close()
		except Exception,ex:
			print Exception,":",ex

	def query_update(self,sqlCommand):
		try:
                        conn = MySQLdb.connect(
                                host = host,
                                user = user,
                                port = port,
                                passwd = passwd
                        )
                        cur=conn.cursor()
                        cur.execute(sqlCommand)
                        conn.commit()
                        cur.close()
                        conn.close()
                except Exception,ex:
                        print Exception,":",ex
