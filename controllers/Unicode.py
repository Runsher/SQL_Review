#coding: utf-8
import chardet
import os

class TransferToUnicode():
	def transferToUnicode(self,filename):
		f = open(filename).read()
		enc = chardet.detect(f)
		try:
			code_type = enc['encoding'].lower()
			f_w = open(filename,"w")
			f_w.write(f.decode(code_type).encode("utf8"))
                except Exception,ex:
                        os.remove(filename)
		
