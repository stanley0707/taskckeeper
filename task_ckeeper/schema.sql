PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS  taskckeeper (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_title TEXT NOT NULL DEFAULT '', 
    task_text TEXT NOT NULL DEFAULT '',
    task_time DATETIME NOT NULL DEFAULT '',
    status INTEGER DEFAULT 0,
    created DATETIME NOT NULL DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (task_id) REFERENCES id_taskckeeper(id) ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS id_taskckeeper(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_title TEXT NOT NULL DEFAULT '', 
    data_text TEXT NOT NULL DEFAULT ''
)
