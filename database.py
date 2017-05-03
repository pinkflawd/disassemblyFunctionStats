#!/usr/bin/env python
# encoding: utf-8

import os.path
import sqlite3


class Database(object):

	def __init__(self):
		try:
			self.localdb = sqlite3.connect(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'fDetectStats.db'))
			# set row factory to Row type for accessing rows as dictionaries
			self.localdb.row_factory = sqlite3.Row
		except:
			print("Connection to DB cant be established.")

	def __del__(self):
		try:
			self.localdb.close()
		except:
			pass

	###########################
	# Base Operations	   #
	###########################

	def select(self, select_string):
		try:
			cursor = self.localdb.cursor()
			cursor.execute(select_string)
		except(Exception) as e:
			print("Error on select %s - %s" % (str(e), select_string))
			return None
		else:
			return cursor

	def insert(self, insert_string):

		try:
			cursor = self.localdb.cursor()
			cursor.execute(insert_string)
		except(Exception) as e:
			print("Error %s - %s" % (str(e), insert_string))
			# print "An Error occurred when executing an insert."
		else:
			self.localdb.commit()
			cursor.close()

	def delete(self, delete_string):
		try:
			cursor = self.localdb.cursor()
			cursor.execute(delete_string)
		except(Exception) as e:
			print("Error %s" % str(e))
			print("An Error occurred when executing a delete.")
		else:
			self.localdb.commit()
			cursor.close()

	def update(self, update_string):
		try:
			cursor = self.localdb.cursor()
			cursor.execute(update_string)
		except:
			print("An Error occurred when executing an update.")
		else:
			self.localdb.commit()
			cursor.close()

	###########################
	# Details			#
	###########################

	def insert_r2(self, sha1, offset, size, name):
		insert_string = "insert into r2_data (sha1, offset, size, name) values ('%s', '%s', %d, '%s')" % (sha1, offset, size, name)
		self.insert(insert_string)
		
	def insert_ida(self, sha1, offset, size, name):
		insert_string = "insert into ida_data (sha1, offset, size, name) values ('%s', '%s', %d, '%s')" % (sha1, offset, size, name)
		self.insert(insert_string)

	###########################
	# Scheme Management	#
	###########################

	def create_scheme(self):

		create_string = """CREATE TABLE r2_data (
							sha1 text,
							offset text,
							size integer,
							name text,
							PRIMARY KEY (sha1, offset)
						)"""
		self.insert(create_string)

		create_string = """CREATE TABLE ida_data (
							sha1 text,
							offset text,
							size integer,
							name text,
							PRIMARY KEY (sha1, offset)
						)"""
		self.insert(create_string)

		print("LOG - Scheme (re)created")

	def flush_all(self):
		self.localdb.execute("VACUUM")
		drop_string = """drop table if exists r2_data"""
		self.delete(drop_string)
		drop_string = """drop table if exists ida_data"""
		self.delete(drop_string)
		print("LOG - All data flushed")
