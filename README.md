# taskckeeper

Hi!

Description: console module for recording, editing and deleting tasks.

language: Python3
db: SQLite3

The DB listens from data/taskckeeper.sqlite (the file is created atomically).
All commands are available from any program cycle

=TASK_CKEEPER SCHEMA =

*arguments:
    
        `cmd`         - variable containing lowercase
        `task_id`    -  variable containing a numeric value or, outside of the call to db,
                       accepts an excluding lowercase value,
                       (The call parameter and column identifier)
        `task_title`  - title marker (the invocation parameter and the column identifier of the db),
        `task_text`   - text marker (the invocation parameter and the column identifier of the db),
        `created`     - time stamp (inversion parameter and column identifier db),
        `actions`     - dictionary containing commands,
        `action`      - variable containing the value of a command from a dictionary,
        `chois`       - variable in function task_delet receiving from the user two values,
        `output_task` - variable containing the request for an insert of all tasks from db.
                      After a cycle in function task_list receives numerical value of length of the list.
        `task`       - variable in the function task_open, contains objects from the tuple.
    
    
    *func logic:
____________________________________________________________________   
    entry     |    __init__.py           |    db.connect.py         
--------------------------------------------------------------------
    main()         task_menu()         
                   menu(params)        
--------------------------------------------------------------------
    menu()                                    get_connection() 
                                                  connection()
                                              init(params)
--------------------------------------------------------------------
    menu()        task_craect(params)         add_task(params) 
-------------------------------------------------------------------- 
    menu()        task_list(params)           find_task_list(params)
--------------------------------------------------------------------
    menu()        task_open(params)           find_task(params)
--------------------------------------------------------------------
    menu()        task_edit(params)           edit_task(params)
--------------------------------------------------------------------
    manu()        task_delet(params)          delet_task(params)
--------------------------------------------------------------------
                  go_menu()             
--------------------------------------------------------------------
                  task_menu()          
--------------------------------------------------------------------
