#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import string

html = """
<html>
 <body>
  <p>%s</p>
 </body>
</html>
"""

def app(environ, start_response):
	d = environ['QUERY_STRING']
	lst = d.split('&')
	lst = map(lambda x: x+'<br>', lst)
	body = html % string.join(lst)
	print(body)
	status = '200 OK'
	headers = [ ('Content-Type', 'text/html'), ('Content-Length', str(len(str(body)))) ]
	start_response(status, headers)
	return body
