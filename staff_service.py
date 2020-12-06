#!/usr/bin/python
import psycopg2
from config import config

def add_staff(staff_name, staff_position):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO staff(staff_name, staff_position, staff_status) VALUES(%s, %s, 1) RETURNING staff_id'
		cur.execute(q, (staff_name, staff_position))	
		staff_id = cur.fetchone()[0]
		conn.commit()
		return staff_id
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def set_status(staff_id, staff_status):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'UPDATE staff SET staff_status = %s WHERE staff_id = %s'
		cur.execute(q, (staff_status, staff_id))	
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_name(staff_name):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM staff WHERE staff_name = %s'
		cur.execute(q, (staff_name))
		data = cur.fetchone()[0]
		return data	
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_position(staff_position):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM staff WHERE staff_position = %s'
		cur.execute(q, (staff_position))
		data = cur.fetchall()
		return data	
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def sel_status(staff_status):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT * FROM staff WHERE staff_status = %s'
		cur.execute(q, (staff_status))
		data = cur.fetchall()
		return data
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

