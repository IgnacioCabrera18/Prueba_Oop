import sqlite3
from typing import List, Dict, Any

class UserRepository:
    def __init__(self, db_name: str = "usuarios_api.db"):
        self.db_name = db_name
        self._create_table()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_table(self):
        conn = self._get_connection()
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                rol TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def add(self, name: str, age: int, rol: str) -> int:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (name, age, rol) VALUES (?, ?, ?)", (name, age, rol))
        conn.commit()
        ultimo_id = cursor.lastrowid
        conn.close()
        return ultimo_id

    def get_all(self) -> List[Dict[str, Any]]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        data = [dict(register) for register in cursor.fetchall()]
        conn.close()
        return data

    def get_by_id(self, user_id: int) -> Dict[str, Any] | None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
        register = cursor.fetchone()
        conn.close()
        return dict(register) if register else None

    def delete(self, user_id: int) -> bool:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        conn.commit()
        register = cursor.rowcount
        conn.close()
        return register > 0
