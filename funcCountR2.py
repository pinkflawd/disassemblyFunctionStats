#!/usr/bin/env python

import r2pipe
import sys
import os
import json
from hashlib import sha1
from time import time
import database

def r2functionlist(path):
	R2PY = r2pipe.open(filepath)

	R2PY.cmd("e asm.lines = false")
	R2PY.cmd("e asm.fcnlines = false")
	R2PY.cmd("e anal.noncode = false")
	R2PY.cmd("e anal.autoname= false")
	R2PY.cmd("e anal.jmptbl = true")
	R2PY.cmd("e anal.hasnext = true")
	R2PY.cmd("e src.null = true")
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
	#mydb.flush_all()
	#mydb.create_scheme()

	for (dirpath, dirnames, filenames) in os.walk(sys.argv[1]):
		for filename in filenames:
			
			# IDA creates .idb and other kind of files during parsing, better name the files after their hashes
			if not '.' in filename:
				filepath = os.path.join(dirpath, filename)

				#start = time()
				
				mysha1 = sha1(open(filepath, 'rb').read()).hexdigest()
				functionList = r2functionlist(filepath)
				
				#end = time()

				# not sure sorting makes sense, but whatevs
				tempdict = {}
				for function in functionList:
					tempdict[hex(function['offset'])] = [function['size'], function['name']]

				for key in sorted(tempdict.keys()):
					mydb.insert_r2(mysha1, key, tempdict[key][0], tempdict[key][1])
					