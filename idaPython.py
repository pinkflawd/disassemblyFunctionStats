#!/usr/bin/env python
# encoding: utf-8

import subprocess
import sys
import os
from time import time


def idaPythonSub(path):
	# In order to get that stuff to run - only static paths, sorry - modify accordingly
	subprocess.call([r'[PATH_TO_IDA]idaq64.exe', '-A', r'-OIDAPython:1;[PATH_TO_IDAPYTHON_SCRIPT]funcCountIDA.py', path])

	
if __name__ == '__main__':

	for (dirpath, dirnames, filenames) in os.walk(sys.argv[1]):
			for filename in filenames:
				if not '.' in filename:
					#start = time()
					filepath = os.path.join(dirpath, filename)
					idaPythonSub(filepath)
					#end = time()