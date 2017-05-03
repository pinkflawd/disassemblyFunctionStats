#!/usr/bin/env python
# encoding: utf-8

from idautils import *
from idc import *
from idaapi import *
from hashlib import sha1
import database

idaapi.autoWait()

mypath = GetInputFilePath()
mysha1 = sha1(open(mypath, 'rb').read()).hexdigest()

mydb = database.Database()
	
funcCount = 0

ea = BeginEA()
for funcea in Functions(SegStart(ea), SegEnd(ea)):
	funcCount = funcCount + 1
	funcSize = FindFuncEnd(funcea) - funcea
	mydb.insert_ida(mysha1, hex(funcea)[:-1], funcSize, GetFunctionName(funcea))
	
idc.Exit(0)