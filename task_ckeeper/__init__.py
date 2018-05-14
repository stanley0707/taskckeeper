
import sys
from task_ckeeper import db_connect
from task_ckeeper import colors
from task_ckeeper import words
from datetime import datetime, timedelta, timezone


def task_creat(cmd, task_id):
	"""  Создание задачи  """
	print("\n Cоздание задачи:\n")
	try:
		task_title = input('\nЗаголовок:\n   ')
		task_text = input('\nЗадача:\n   ')
		days, hours = input('время на выполнение (дни часы):\n ').split()
		days = int(days)
		hours = int(hours)
		task_time = datetime.now(timezone.utc) + timedelta(days=days, hours=hours)
		task_time = task_time.astimezone()
		with db_connect.get_connection() as conn:
				task = db_connect.add_task(conn, task_title, task_text, task_time)
		if len(task_title) == 0 or len(task_text) == 0:
			print(colors.color.Red +  'все поля должны быть заполнены' + colors.color.END)
			main()
	except ValueError:
		main()


def update_task_status(cmd, task_id):
	"""  Редактор cтатуса """
	status = 1
	with db_connect.get_connection() as conn:
		edit = db_connect.update_status(conn, task_id, status)

def res_task(cmd, task_id):
	""" рестарт задачи """
	try:
		with db_connect.get_connection() as conn:
			task = db_connect.find_task(conn, task_id)
			task_time = task[5]
			edit = db_connect.restart(conn, task_id, task_time)
	except TypeError:
		print(colors.color.Red  + '\n Вы еще не создали задачу под таким номером\n' + colors.color.END)
		main()

def task_list(cmd, task_id):
	""" Список задач """
	
	print(colors.color.Cyan + '\n откройте задачу по номеру : open (num)\n', 30 * '-' + colors.color.END)
	with db_connect.get_connection() as conn:
		output_task = db_connect.find_task_list(conn,)
		for i in output_task:
			
			delta_time = str(datetime.now())
			time = i[2]
			time_now = int(delta_time[8:10] + delta_time[11:13])
			time_task = int(time[8:10] + time[11:13])
			
			delta_days = int(time[8:10]) - int(delta_time[8:10])
			delta_hours = int(time[11:13]) - int(delta_time[11:13])
			delta_out =  str(delta_days) + ' ' + str(words.days(delta_days)) + ' ' + str(delta_hours) + ' ' + str(words.hours(delta_hours))
			
			if time_now >= time_task and i[3] == 0:
				u_out = colors.color.Red + 'не выполнено' + colors.color.END
			elif time_now < time_task and i[3] == 0:
				u_out = colors.color.Yellow + 'выполненяется (deadline:' + delta_out + ')' + colors.color.END
			else:
				u_out = colors.color.Cyan + 'выполнено' + colors.color.END
			print(i[0], i[1], i[4], u_out ,'\n')
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
			print(" Время: ",  colors.color.Yellow  + str(task[5]),'\n' + colors.color.END)
			print(" deadline: ",  colors.color.Yellow  + str(task[3]),'\n' + colors.color.END)
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
	new  (ключ)          Создать задачу,
	open (ключ)          Открыть задачу,
	edit (ключ)          Редактировать задачу,
	del  (ключ)          Удалить задачу,
	done (ключ)			 отметить как выполеную,
	rest (ключ)			 начать заново,
	list open            Отобразить список задач,
	menu open            Меню,
	exit -g              Выйти из программы
	"""
	)

def menu(actions):
	""" обработчик команд """
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
    'done': update_task_status,
    'rest': res_task
    }
