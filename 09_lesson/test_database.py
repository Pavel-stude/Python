from sqlalchemy import text
from database import db


def test_insert_user():
    connection = db.connect()
    transaction = connection.begin()

    insert_sql = text("""
        INSERT INTO users (name, age)
        VALUES (:name, :age)
    """)
    connection.execute(insert_sql, {"name": "Test_User", "age": 20})

    select_sql = text("""
        SELECT * FROM users
        WHERE name = :name
    """)
    result = connection.execute(select_sql, {"name": "Test_User"}).fetchone()

    assert result is not None

    transaction.commit()
    connection.close()


def test_update_user():
    connection = db.connect()
    transaction = connection.begin()

    update_sql = text("""
        UPDATE users
        SET age = :age
        WHERE name = :name
    """)
    connection.execute(update_sql, {"age": 30, "name": "Test_User"})

    select_sql = text("""
        SELECT age FROM users
        WHERE name = :name
    """)
    result = connection.execute(select_sql, {"name": "Test_User"}).fetchone()

    assert result[0] == 30

    transaction.commit()
    connection.close()


def test_delete_user():
    connection = db.connect()
    transaction = connection.begin()

    delete_sql = text("""
        DELETE FROM users
        WHERE name = :name
    """)
    connection.execute(delete_sql, {"name": "Test_User"})

    select_sql = text("""
        SELECT * FROM users
        WHERE name = :name
    """)
    result = connection.execute(select_sql, {"name": "Test_User"}).fetchone()

    assert result is None

    transaction.commit()
    connection.close()