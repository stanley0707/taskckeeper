import os.path as Path
import sqlite3
from task_ckeeper import colors
from task_ckeeper import colors

""" константы обращения """
SQL_INSERT_TASK = 'INSERT INTO taskckeeper(task_id, task_title, task_text) VALUES (?,?,?)' 
SQL_SELECT_ALL = """
	SELECT 
	task_id, task_title, task_text, created
	FROM
	taskckeeper
"""
SQL_SELECT_TASK_BY_TITLE = SQL_SELECT_ALL + ' WHERE task_title=?'
SQL_SELECT_TASK_TITLE_BY_ALL = 'SELECT task_id, task_title, created FROM taskckeeper'
SQL_SELECT_TASK_TITLE_BY_ID = 'SELECT * FROM taskckeeper WHERE task_id=?'
SQL_UPDATE_TASK = 'UPDATE  taskckeeper SET task_title=?, task_text=? WHERE task_id=?'
SQL_DELET_TASK = 'DELETE FROM taskckeeper WHERE task_id=?'


def connection(db_name=None):
	""" обработчик обращения и создание файла """
	while 1:
		if db_name is None:
			db_name = ':memory:'
		conn = sqlite3.connect(db_name)
		return conn
	conn.close()

""" установка соединения через обработчик """
get_connection = lambda: connection('data/taskckeeper.sqlite')
 	

def init(conn):
	""" инициализация обращения по параметрам SQL """
	script_path = Path.join(Path.dirname(__file__), 'schema.sql') 
	with conn, open(script_path) as f:
		conn.executescript(f.read())


def add_task(conn, task_id, task_title, task_text):
	""" загрузка  задачи в db  """
	try:
		with conn:
			cursor = conn.execute(SQL_INSERT_TASK, (task_id, task_title, task_text))
			print(colors.color.Cyan + '\n',"="*16," DONE  ","="*16, '\n', "="*11," задача сохранена ", "="*11, '\n' + colors.color.END)
			conn.commit()
	except sqlite3.IntegrityError:
		print(colors.color.Red + 'id задачи должен быть числом' + colors.color.END)
	

""" вывод  """

def find_task_list(conn):
	""" Вывод задач по заголовкам"""
	try:
		with conn:
			conn = conn.execute(SQL_SELECT_TASK_TITLE_BY_ALL)
			while 1:
				output_task = conn.fetchall() 
				if output_task == None:
					break
				#conn.close()
				return output_task
			conn.commit()
	except  TypeError:
		print(" создайте первое задание с Tasckceeper ")


def find_task(conn, task_id):
	""" Вывод задачи по id"""
	try:
		with conn:
			conn = conn.execute(SQL_SELECT_TASK_TITLE_BY_ID, (task_id,))
			while 1:
				task_id = conn.fetchone() 
				if task_id == None:
					break
				#conn.close()
				return task_id
			conn.commit()
	except AttributeError:
		print(" ")


def edit_task(conn, task_id, task_title, task_text):
	""" редактирование """
	title = task_title
	text = task_text
	if not title:
		raise Warning("Заголовод должен состоять хотя бы из одного символа")
	elif not text:
		raise Warning("Текст задачи должен состоять из хотя-бы из одного символа")
	with conn:
		cursor = conn.execute(SQL_UPDATE_TASK, (task_title, task_text, task_id))
		print(colors.color.Cyan + '\n',"="*16," DONE  ","="*16, '\n', "="*11," задача  сохранена ", "="*11, '\n' + colors.color.END)
		conn.commit()


def delet_task(conn, task_id):
	""" удаление """
	with conn:
		print(task_id)
		cursor = conn.execute(SQL_DELET_TASK, (task_id,))
		print(colors.color.Cyan + '\n',"="*16," DONE  ","="*16, '\n', "="*11," задача удалена ", "="*11, '\n' + colors.color.END)
		conn.commit()






