# taskckeeper

Description: console module for recording, editing and deleting tasks.

language: Python3

The DB listens from data/taskckeeper.sqlite (the file is created atomically).
All commands are available from any program cycle

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
    main():                                         get_connection <----> connection()   <----->  data/taskckeeper.sqlite                         
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