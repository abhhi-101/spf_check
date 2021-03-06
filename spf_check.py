#!/bin/python3

import requests
import sys
import os
import optparse

parser = optparse.OptionParser()
parser.add_option('-d', '--domain', dest='domain', help='To Find SOF Record of domain Specified', metavar="example.com")
parser.add_option('-f', '--file', dest='domains_file', help='File Containing list of Domains', metavar="file.txt")
(options, arguments) = parser.parse_args()
core =('https://www.kitterman.com/spf/getspf3.py')
print('''
	SPF Validator
		- Made with <3 by abhhi
''')

def spf_check(domain):
	body = {'serial':'fred12','domain':domain}
	request = requests.post(core,data = body)
	response = request.text
	outFile = open("spf_result.txt","a")
	if 'No valid SPF record found' in response:
		print("[+] No SPF at : " + domain + "; Report it!!!")
		outFile.write("[+] No SPF at : "+domain)
		outFile.write("\n")
	else:
		print("[-] Forget it for " + domain + "!!!")
		outFile.write("[-] Forget it for "+domain+"!!!")
		outFile.write("\n")
	outFile.close()
if len(sys.argv) < 2 :
	print("Use : -h or --help for usage!!")
	sys.exit()
elif sys.argv[1] == '-f':
	domains_file = open(options.domains_file,'r')
	for domain in domains_file:
		spf_check(domain.rstrip('\n'))
elif sys.argv[1] =='-d':
	domain = options.domain
	spf_check(domain)
else:
	print("Use : -h or --help for usage!!")
