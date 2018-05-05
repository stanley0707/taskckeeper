CREATE TABLE IF NOT EXISTS  taskckeeper (
        task_id INTEGER PRIMARY KEY,
        task_title TEXT NOT NULL DEFAULT '', 
        task_text TEXT NOT NULL DEFAULT '',
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
