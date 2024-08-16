import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the path to the database file
db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'todos.db')
engine = create_engine(f'sqlite:///{db_path}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define models
Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String, unique=True, index=True)
#
#     def __repr__(self):
#         return f"<User(name={self.name}, email={self.email})>"

class TodoList(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    progress = Column(Integer)  # 0 = not started, 1 = in progress, 2 = completed

    def __init__(self, *, task):
        self.task = task
        self.progress = 0

    def __repr__(self):
        return f"<Task(task={self.task}, progress={self.progress})>"


# Create tables
Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()


if __name__ == "__main__":
    db = get_session()

    try:
        task = TodoList(task="Finish this project")

        db.add(task)
        db.commit()

        result = db.query(TodoList).all()
        for r in result:
            print(r)
    finally:
        db.close()