
import sqlite3

DATABASE = "notes.db"

def get_connection():
    return sqlite3.connect(DATABASE)

def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def add_note(title, content):
    conn = get_connection()

    conn.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content)
    )

    conn.commit()
    conn.close()

def get_notes():
    conn = get_connection()
    conn.row_factory = sqlite3.Row

    notes = conn.execute(
        "SELECT * FROM notes ORDER BY id DESC"
    ).fetchall()

    conn.close()
    return notes

def delete_note(note_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )

    conn.commit()
    conn.close()
