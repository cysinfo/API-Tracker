#!/usr/bin/python

"""
A simple server
"""

from socket import *
import sys
import struct

def net_on(log_file):
	host = ''
	port = 50000
	backlog = 10
	size = 1024
	s = socket(AF_INET, SOCK_STREAM,0)
	s.bind((host,port))
	s.listen(backlog)
	fp = open(log_file,'a')
	while 1:
	    client, address = s.accept()
	    data = client.recv(size)
	    if data:
	        print data
	        fp.write(data)
	        fp.write("\n")

def main():
	if len(sys.argv) < 2:
		print "server.py log_file"
		sys.exit(0)
	log_file = sys.argv[1]
	net_on(log_file)

if __name__ == '__main__':
	main()		    

