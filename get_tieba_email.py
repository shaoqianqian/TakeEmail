#coding=utf-8
#读取web页面数据接口
import urllib
#正则表达式
import re
import socket
import time
import os
socket.setdefaulttimeout(10)

#定义一个getHtml()函数
def getHtml(url):
	try:
		page = urllib.urlopen(url)
		html = page.read()
		print "get response"
		

		if ("该帖已被删除" in html) or "该吧被合并您所访问的贴子无法显示" in html:
			print "404"
			return ""
		else:
			print page.code
			return html
	except Exception, e:
		exit
    
	
	
	



def getEmail(html):
	emailRegex = r'[0-9a-zA-Z_]+@[0-9a-zA-Z._]+\.[0-9a-zA-Z._]+'  
	emailre =re.compile(emailRegex);
	email = re.findall(emailre,html)
	print email
	return email






if __name__ == '__main__':
	dirname=os.path.dirname(os.path.realpath(__file__))
	name_prefix=dirname.split("\\")[-1];
	emailpath=dirname[0:dirname.index(name_prefix,0,len(dirname))]
	try:
		fileread = open(dirname+'/index.txt')
		line=fileread.readline()
		start=long(line)
	except Exception, e:
		start=long(name_prefix)
		
	
	print start
	end=start+10
	for x in xrange(start,end):
		filename=time.strftime("%Y%m%d",time.localtime())
		f = open(emailpath+name_prefix+"_"+filename+'.txt','a+')
		oldemail=""
		for y in xrange(1,500):
			url="http://tieba.baidu.com/p/"+str(x)+"?pn="+str(y)
			print url
			html=getHtml(url)
			if html=="":
				break

			emails=getEmail(html)
			for email in emails:
				if oldemail==email:
					continue
				else:
					oldemail=email

				f.write(email+'\n')
				f.flush
			#判断是否有下一页
			if "下一页" in html and "尾页" in html:
				print "next page"
				continue
			else:
				print "not next page"
				break
		f.flush
		f.close
	filewrite = open(dirname+'/index.txt','w')
	filewrite.write(str(end))
exit()