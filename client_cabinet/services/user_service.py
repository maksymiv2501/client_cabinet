from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_connection


def create_test_admin():
    conn = get_connection()

    user = conn.execute(
        "SELECT id FROM users WHERE email = ?",
        ("admin@gmail.ua",)
    ).fetchone()

    if not user:
        conn.execute("""
            INSERT INTO users (email, password, name, role)
            VALUES (?, ?, ?, ?)
        """, (
            "admin@gmail.ua",
            generate_password_hash("1234"),
            "Адміністратор",
            "financial"
        ))
        conn.commit()

    conn.close()


def authenticate_user(email, password):
    conn = get_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    conn.close()

    if user and check_password_hash(user["password"], password):
        return user

    return None
