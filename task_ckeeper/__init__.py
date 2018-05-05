
"""
=================== TASK_CKEEPER SCHEMA ====================

arguments:
	cmd         - переменная содержащая строчное обращение
	
	task_id     - переменная содержащая числовое значение или, вне обращения к db  
				  принимает исключающие строчное значние.
				  (пааметр обращения и идентификатор столбца бд)
				  
	task_title  - маркер заголовка (параметр обращения и идентификатор столбца бд)
	task_text   - маркер текста (параметр обращения и идентификатор столбца бд)
	created     - марке времени (параметр обращения и идентификатор столбца бд
	
	actions     - словарь содержащий команды
	action      - переменная содержащая значение команды из словаря
	chois       - переменная в функции task_delet принимающая от юзера два значения
	output_task - переменная содержащая в себе запрос на инсерт всех задач из db,
				  после цикла в функции task_list получает числовое значние длинны списка.
	task        - переменная в функци task_open, содержит в себе объекты из кортежа.

logic:

__init__.py                                       db.connect.py         
 	main():				                            get_connection <----> connection() <----->  data/taskckeeper.sqlite					        
		  											^                                              ^
		menu(actions):        <---------------->    init() ----> schema.sql                        |
				                                                                                   |
			task_craect()      ---------------->    add_task(params) ---------------- conn --------+                          
			task_list()       <---------------->    find_task_list(params)  |           |
			task_open()       <---------------->    find_task(params)       |           |
			task_edit()       <---------------->    edit_task(params)       |___________|
			task_delet()      <---------------->    delet_task(params)      |
			task_exit()       
		    go_menu()
		    task_menu()
		
		task_menu()

"""

import sys
from task_ckeeper import db_connect
from task_ckeeper import colors



def task_creat(cmd, task_id):
	""" Создание задачи  """
	print("\n Cоздание задачи:\n")
	try:
		print('id:', task_id)
		task_title = input('\nЗаголовок:\n   ')
		task_text = input('\nЗадача:\n   ')
		with db_connect.get_connection() as conn:
				task = db_connect.add_task(conn, task_id, task_title, task_text)
		if len(task_title) == 0 or len(task_text) == 0:
			print(colors.color.Red +  'все поля должны быть заполнены' + colors.color.END)
			main()
	except ValueError:
		main()




def task_list(cmd, task_id):
	""" Список задач """
	print(colors.color.Cyan + '\n откройте задачу по номеру : open (num)\n', 30 * '-' + colors.color.END)
	with db_connect.get_connection() as conn:
		output_task = db_connect.find_task_list(conn,)
		for i in output_task:
			print(i,'\n')
		print(colors.color.Cyan + 'всего: ', len(output_task) ,' \n', 30 * '-' + colors.color.END)
	try:	
		if cmd <= len(output_task):
			task_open(cmd)

		else:
			print( colors.color.Red + 'Вы еще не создали задачу с таким номером' + colors.color.END) 
		menu(actions, task_id)
	except TypeError:
		cmd = str(cmd)


def task_open(cmd, task_id):
	"""  Открыть задачу  """
	try:
		with db_connect.get_connection() as conn:
			task = db_connect.find_task(conn, task_id)
			print(colors.color.Cyan + "\nЗАДАЧА - ", task_id,": " + colors.color.END)
			print ( colors.color.Cyan  + 30 * '-' + colors.color.END)
			print(" Заголовок: ", colors.color.Yellow  + task[1],'\n' + colors.color.END)
			print(" Задча: ",  colors.color.Yellow  + task[2],'\n' + colors.color.END)
			print(" Время: ",  colors.color.Yellow  + task[3],'\n' + colors.color.END)
			print (30 * '-')
			print("""
	del (num) - удалить задачу,
	edit (num) - редактировать задачу,
	menu open - menu
	""")		
			menu(actions)			
			main()
	except TypeError:
		print(colors.color.Red  + '\n Вы еще не создали задачу под таким номером\n' + colors.color.END)
		main()


def task_edit(cmd, task_id):
	"""  Редактор задачи """
	print (30 * '-')
	print("редактирование задачи -", task_id, '\n')
	print (30 * '-')
	task_title = input('\nЗаголовок:\n   ')
	task_text = input('\nЗадача:\n   ')
	with db_connect.get_connection() as conn:
		edit = db_connect.edit_task(conn, task_id, task_title, task_text)
 

def task_delet(cmd, task_id):
    """ Удаление задачи  """
    print(colors.color.Red + "Внимание! Вы действительно хотитет удалить задачу? \ny/n" + colors.color.END)
    chois = input()
    if chois == 'y':
        with db_connect.get_connection() as conn:
            delet = db_connect.delet_task(conn, task_id)
            main()
    else:
        task_list(actions)





def go_menu(cmd, task_id):
    """ Возврат в меню """
    main()

def task_exit(cmd, task_id):
	""" выход  из редактора """
	print('До встречи! Помни свои задачи!!!')
	sys.exit()

def task_menu():
	"""  приветсвие меню  """
	print (colors.color.White + '\n', 30 * '-' + colors.color.END)
	print (colors.color.White + "  T A S K - C K E E P E R   menu " + colors.color.END)
	print (colors.color.White + 30 * '-' + colors.color.END)
	print(
	"""
	new  (num)          Создать задачу,
	open (num)          Открыть задачу,
	edit (num)          Редактировать задачу,
	del  (num)          Удалить задачу,
	list open           Отобразить список задач,
	menu open           Меню,
	exit -g             Выйти из программы
	"""
	)

def menu(actions):
	""" -------  обработчик команд ------- """
	with db_connect.get_connection() as conn:
		db_connect.init(conn)
	try:	
		while 1:
			cmd, task_id = input('введите команду: ').split()
			action = actions.get(cmd)
			try:
				task_id = int(task_id)
				if actions:
					action(cmd, task_id)
			except ValueError:
				task_id = str(task_id)
				action(cmd, task_id)

	except ValueError:
		print(colors.color.Red +'неизвестная команда'+ colors.color.END)
		menu(actions)

def main():
	task_menu()
	menu(actions)

actions = {
    'new' : task_creat,
    'open': task_open,
    'menu': go_menu,
    'list': task_list,
    'exit': task_exit,
    'edit': task_edit,
    'del' : task_delet,
    }
		
  