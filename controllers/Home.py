#coding:utf-8
import os.path
import tornado.httpserver
import tornado.web
import tornado.options
import tornado.ioloop

class BaseHandler(tornado.web.RequestHandler):
        def get(self):
                pass;

class IndexHandler(BaseHandler):
#        @tornado.web.authenticated
        def get(self):
#                name = tornado.escape.xhtml_escape(self.current_user)
                self.render("index.html",
                )
