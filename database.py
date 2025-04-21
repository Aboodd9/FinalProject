import sqlite3

DB_NAME = 'iot_data.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_insecure(device_id, message):
    """Vulnerable to SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    query = f"INSERT INTO sensor_logs (device_id, message) VALUES ('{device_id}', '{message}')"
    c.execute(query)
    conn.commit()
    conn.close()

def insert_secure(device_id, message):
    """Secure: uses parameterized queries"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO sensor_logs (device_id, message) VALUES (?, ?)", (device_id, message))
    conn.commit()
    conn.close()

def view_logs():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM sensor_logs")
    rows = c.fetchall()
    conn.close()
    return rows
