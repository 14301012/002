# -*- coding:utf-8 -*-
import os

def application(environ, start_response):
    
    if ".html" in environ['PATH_INFO']:
         
         filename =environ['PATH_INFO'][1:]
         
         if os.path.exists(filename):
             start_response('200 OK', [('Content-Type', 'text/html')])
             return open(filename).read( )
         else:
             start_response('404 NotFound', [('Content-Type', 'text/html')])
             return '404 NotFound!'    
         
    else:
         start_response('200 OK', [('Content-Type', 'text/html')])
         return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] )