import sqlite3
from task import Task


class Database:
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL
            )
        """)
        self.connection.commit()
        cursor.close()

    def insert_task(self, title):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, 0))
        self.connection.commit()
        cursor.close()

    def get_all_tasks(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, title, done FROM tasks")
        rows = cursor.fetchall()
        cursor.close()
        tasks = []
        for row in rows:
            task = Task(row[0], row[1], row[2])
            tasks.append(task)
        return tasks

    def mark_done(self, task_id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        self.connection.commit()
        cursor.close()

    def delete_task(self, task_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.connection.commit()
        cursor.close()

    def close(self):
        self.connection.close()
