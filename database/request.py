from database.connect import Connection
import hashlib

def authorization(login, password):
    """Авторизация"""
    
    conn = Connection()
    cursor = conn.cursor_dict
    
    has_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute(f"SELECT * FROM users WHERE login='{login}' AND password='{has_password}'")
    
    result = cursor.fetchone()
    
    conn.commit()
    conn.close()
    return result

def registration(login, password):
    """Регистрация"""
    
    conn = Connection()
    cursor = conn.cursor_dict
    
    has_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute(f"SELECT * FROM users WHERE login='{login}'")
    
    if cursor.fetchone():
        conn.commit()
        conn.close()
        return False
    else:
        cursor.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{has_password}')")
        conn.commit()
        conn.close()
        return True