import sqlite3

def init_db():
    conn = sqlite3.connect("scans.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            results TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_scan(target, results):
    init_db()
    conn = sqlite3.connect("scans.db")
    c = conn.cursor()
    c.execute("INSERT INTO scans (target, results) VALUES (?, ?)",
              (target, str(results)))
    conn.commit()
    conn.close()
