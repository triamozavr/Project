#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
	commands = (
		"""
		CREATE TABLE items (
			item_id SERIAL PRIMARY KEY,
			item_name VARCHAR(255) NOT NULL,
			item_status VARCHAR(255) NOT NULL,
			item_has_passport BOOLEAN,
			item_b_place VARCHAR(255),
			item_b_date DATE,
			item_warranty DATE
		)
		""",
		""" 
		CREATE TABLE staff (
			staff_id SERIAL PRIMARY KEY,
			staff_name VARCHAR(255) NOT NULL,
			staff_position VARCHAR(255) NOT NULL
		);
		""",
		"""
		CREATE TABLE items_staff (
			staff_id INTEGER NOT NULL,
			item_id INTEGER NOT NULL,
			PRIMARY KEY (staff_id , item_id),
			FOREIGN KEY (staff_id)
				REFERENCES staff (staff_id)
				ON UPDATE CASCADE ON DELETE CASCADE,
			FOREIGN KEY (item_id)
				REFERENCES items (item_id)
				ON UPDATE CASCADE ON DELETE CASCADE,
			link_dt DATE
		);
		""",
		"""
		CREATE TABLE history (
			event_name VARCHAR(255) NOT NULL,
			event_date DATE,
			staff_id INTEGER NOT NULL,
			item_id INTEGER NOT NULL,
			PRIMARY KEY (staff_id , item_id),
			FOREIGN KEY (staff_id)
				REFERENCES staff (staff_id)
				ON UPDATE CASCADE ON DELETE CASCADE,
			FOREIGN KEY (item_id)
				REFERENCES items (item_id)
				ON UPDATE CASCADE ON DELETE CASCADE
					
		);
		""",
		"""
		CREATE TABLE license (
			l_name VARCHAR(255) NOT NULL,
			l_exp DATE,
			item_id INTEGER NOT NULL PRIMARY KEY,
			FOREIGN KEY (item_id)
				REFERENCES items (item_id)
				ON UPDATE CASCADE ON DELETE CASCADE
					
		);
		""")


	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		for command in commands:
			cur.execute(command)
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	create_tables()
