#!/usr/bin/python
import psycopg2
import datetime
from config import config

def add_link(item_id, staff_id, link_dt):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO items_staff(item_id, staff_id, link_dt) VALUES(%s, %s, %s)'
		cur.execute(q, (item_id, staff_id, link_dt))	
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_item(item_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM items_staff WHERE item_id = %s'
		cur.execute(q, (item_id,))	
		data = cur.fetchall()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_staff(staff_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM items_staff WHERE staff_id = %s'
		cur.execute(q, (staff_id,))	
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
		q = 'DELETE FROM items_staff WHERE link_dt = %s'
		cur.execute(q, (date,))	
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
