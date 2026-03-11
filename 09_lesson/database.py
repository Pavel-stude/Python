from sqlalchemy import create_engine

db_connection_string = "postgresql://postgres:qwerty@localhost:5432/postgres"
db = create_engine(db_connection_string)