#!/usr/bin/python
import psycopg2
import datetime
from config import config

def add_event(item_id, staff_id, event_name, event_date):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO history(item_id, staff_id, event_name, event_date) VALUES(%s, %s, %s, %s)'
		cur.execute(q, (item_id, staff_id, event_name, event_date))	
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
		q = 'SELECT * FROM history WHERE item_id = %s'
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
		q = 'SELECT * FROM history WHERE staff_id = %s'
		cur.execute(q, (staff_id,))	
		data = cur.fetchall()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_name(event_name):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM history WHERE event_name = %s'
		cur.execute(q, (event_name,))	
		data = cur.fetchall()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def del_name(event_name):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'DELETE FROM history WHERE event_name = %s'
		cur.execute(q, (event_name,))	
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
