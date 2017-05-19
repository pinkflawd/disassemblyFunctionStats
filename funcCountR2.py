#!/usr/bin/env python

import r2pipe
import sys
import os
import json
from hashlib import sha1
from time import time
import database

def r2functionlist(path):

	global R2PY
	R2PY = r2pipe.open(filepath)

	R2PY.cmd("e asm.lines = false")
	R2PY.cmd("e asm.fcnlines = false")
	R2PY.cmd("e anal.noncode = false")
	R2PY.cmd("e anal.autoname= false")
	R2PY.cmd("e anal.jmptbl = true")
	R2PY.cmd("e anal.hasnext = true")
	#R2PY.cmd(".aab")
	R2PY.cmd("aaa")

	functions = R2PY.cmd("aflj")
	
	if functions:
		functionList = json.loads(functions)
	else:
		functionList = []
	
	return functionList

if __name__ == '__main__':

	mydb = database.Database()

	# for a fresh start, flush the DB
	mydb.flush_all()
	mydb.create_scheme()

	for (dirpath, dirnames, filenames) in os.walk(sys.argv[1]):
		for filename in filenames:
			
			# IDA creates .idb and other kind of files during parsing, better name the files after their hashes
			if '.exe' in filename or '.dll' in filename:
				filepath = os.path.join(dirpath, filename)

				#start = time()
				
				mysha1 = sha1(open(filepath, 'rb').read()).hexdigest()
				mydb.insert_sample(mysha1, filename, os.path.getsize(filepath))
				
				functionList = r2functionlist(filepath)
				
				#end = time()

				# not sure sorting makes sense, but whatevs
				tempdict = {}
				for function in functionList:
					temp = R2PY.cmd("pxf @ " + hex(function['offset']))
					epbytes = temp.split('\n')[1].split()[1:-1]
					
					#gadgets = epbytes.split()
					thehex = []
					for gad in epbytes:
						if len(gad) == 4:
							try:
								int(gad, 16)
								thehex.append(gad)
							except:
								pass
								
					print ''.join(thehex)
					#print ''.join(epbytes)[:32]
					#print epbytes.split()[1:-1]
					tempdict[hex(function['offset'])] = [function['realsz'], function['name'], ''.join(thehex)]

				for key in sorted(tempdict.keys()):
					mydb.insert_r2(mysha1, key, tempdict[key][0], tempdict[key][1], tempdict[key][2])
					