#!/usr/bin/python
import psycopg2
import datetime
from config import config

def add_license(item_id, l_name, l_exp):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO license(item_id, l_name, l_exp) VALUES(%s, %s, %s)'
		cur.execute(q, (item_id, l_name, l_exp))	
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_id(item_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM license WHERE item_id = %s'
		cur.execute(q, (item_id))
		data = cur.fetchone()[0]
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_name(l_name):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM license WHERE l_name = %s'
		cur.execute(q, (l_name))
		data = cur.fetchall()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def del_date(date):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'DELETE FROM license WHERE l_exp = %s'
		cur.execute(q, (date,))
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
