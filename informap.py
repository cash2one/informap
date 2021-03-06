#!/usr/bin/python
#by kttzd
#coding:utf-8
import os
import sys
import getopt
from data.infor_class import scan
from data.CDN import cdn
from data.BaiduHaking import getSub
def main():
	try:
		opts,args=getopt.getopt(sys.argv[1:],"yh:i:u:c:d:t:b:",["help","host=","ip=","url=","c=","dns=","cdn=","baidu="])
	except getopt.GetoptError:
		print "--------"
	_host=None
	_ip=None
	_url=None
	_c=None
	_d=None
	_t=None
	_b=None
	for name,value in opts:
		if name in ("-y","--help"):
			
			sys.exit()

		elif name in ("-h","--host"):
			_host=value
		elif name in ("-i","--ip"):
			_ip=value
		elif name in ("-u","--url"):
			_url=value
		elif name in ("-c","--c"):
			_c=value
		elif name in ("-d","--dns"):
			_d=value
		elif name in ("-t","--cdn"):
			_t=value
		elif name in ("-b","--baidu"):
			_b=value
	if _host:
		
		host=scan(_host)
		#host.getDnsZone()
		a=host.getSubDomains()
		print a["subdomains"]
		for host in  a["subdomains"]:
			h=cdn(host)
			h.getCdn()
	if _d:
		host=scan()
		host.getDnsZone(host=_d)
	if _ip:
		ip=scan(_ip)
		print ip.getFromChinaZ()
		#print ip.getAsNum()
	if _url:
		url=scan(_url)
	if _c:
		with open("config/1.txt") as f:
			config=f.readlines()[0].strip("\n")
		getC=scan()
		h=getC.getC(ip=_c,config=config)
		print h
		#for key in h.keys():
		#	print getC.getFromChinaZ(ip=key)
	if _t:
		with open(_t) as f:
			config=f.readlines()
		for host in config:
			host.strip("\n")
			h=cdn(host)
			h.getCdn()
	if _b:
		try:
			getSub(_b)
		except:
			print "sorry something wrong"
if __name__=="__main__":
	main()
