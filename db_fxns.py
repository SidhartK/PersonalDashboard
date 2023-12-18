import sqlite3
import uuid
import datetime
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

class Task:
	TYPES = {
		"id": "TEXT",
		"name": "TEXT",
		"due_at": "DATETIME",
		"created_at": "DATETIME",
		"status": "TEXT",
		"area": "TEXT",
		"priority": "TEXT",
		"description": "TEXT",
		"parent": "TEXT"
	}

	OPTIONS = {
		"status": ["To-Do","Done"],
		"priority": ["Low","Medium","High"]
	}

	@classmethod
	def get_types(cls):
		return cls.TYPES

	@classmethod 
	def get_key_list(cls):
		return list(cls.TYPES.keys())
	
	@classmethod
	def get_key_names(cls):
		return ",".join(cls.get_key_list())
	
	@classmethod
	def get_template(cls):
		return ",".join([f"{key} {cls.TYPES[key]}" for key in cls.get_key_list()])
	
	created_date = datetime.datetime.now()
	def __init__(self, name, due_at, created_at=datetime.datetime.now(), status=OPTIONS["status"][0], area="", priority=OPTIONS["priority"][0], description="", parent="", id=None):
		self.id = str(uuid.uuid4()) if id is None else id
		self.name = name
		self.status = status
		self.due_at = due_at
		self.created_at = created_at
		self.area = area
		self.priority = priority
		self.description = description
		self.parent = parent

	@property
	def values(self):
		return tuple([getattr(self, key) for key in Task.get_key_list()])

	
def create_table():
	c.execute(f"CREATE TABLE IF NOT EXISTS taskstable({Task.get_template()})")


def add_data(task):
	c.execute(f"INSERT INTO taskstable({Task.get_key_names()}) VALUES ({','.join(['?' for _ in Task.get_key_list()])})",task.values)
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM taskstable')
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM taskstable')
	data = c.fetchall()
	return data

def get_task_by_id(task):
	c.execute("SELECT * FROM taskstable WHERE id=?",(task.id))
	data = c.fetchall()
	return data

def get_task_by_name(task):
	c.execute("SELECT * FROM taskstable WHERE name=?",(task.name))
	data = c.fetchall()
	return data

def get_task_by_status(task):
	c.execute("SELECT * FROM taskstable WHERE status=?",(task.status))
	data = c.fetchall()
	return data

def get_task_by_area(task):
	c.execute("SELECT * FROM taskstable WHERE area=?",(task.area))
	data = c.fetchall()
	return data

def get_task_by_priority(task):
	c.execute("SELECT * FROM taskstable WHERE priority=?",(task.priority))
	data = c.fetchall()
	return data


def edit_task_data(new_task, old_task):
	c.execute(f"UPDATE taskstable SET {','.join([key_name + '=?' for key_name in Task.get_key_list()])} WHERE id=?",(*new_task.values, old_task.id))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(task):
	c.execute("DELETE FROM taskstable WHERE id=?",(task.id))
	conn.commit()


if __name__ == '__main__':
	task = Task("test", "Done", "2021-01-01", "Area", "High", "This is a test item")
	import pdb; pdb.set_trace()