#!/usr/bin/python
import psycopg2
from config import config
import datetime

def add_item(item_name, item_status, item_has_passport):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO items(item_name, item_status, item_has_passport) VALUES(%s, %s, %s) RETURNING item_id'
		cur.execute(q, (item_name, item_status, item_has_passport))	
		item_id = cur.fetchone()[0]
		conn.commit()
		return item_id
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def add_sec(item_id, item_b_place, item_b_date, item_warranty):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'UPDATE items SET '
		q_mid = str()
		l = list()
		if len(item_b_place) != 0:
			q_mid += 'item_b_place = %s,'
			l.append(item_b_place)
		if len(item_b_date) != 0:
			q_mid += 'item_b_date = %s,'
			l.append(item_b_date)
		if len(item_warranty) != 0:
			q_mid += 'item_warranty = %s,'
			l.append(item_warranty)
		l.append(item_id)
		q_mid = q_mid[:-1]
		q_end = ' WHERE item_id = %s'
		cur.execute(q + q_mid + q_end, l)
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
		q = 'SELECT * FROM items WHERE item_id = %s'
		conn.execute(q, (item_id,))
		data = cur.fetchone()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_name(item_name):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM items WHERE item_name = %s'
		conn.execute(q, (item_name,))
		data = cur.fetchone()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_status(item_status):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM items WHERE item_status = %s'
		conn.execute(q, (item_status,))
		data = cur.fetchall()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
 
def del_id(item_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'DELETE FROM items WHERE item_id = %s'
		cur.execute(q, (item_id,))
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_all():
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM items'
		conn.execute(q)
		data = cur.fetchall()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
