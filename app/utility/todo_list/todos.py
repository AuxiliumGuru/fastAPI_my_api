from app.utility.todo_list.todos_sqlAlchemy import get_session, TodoList  # User


# def try_():
#     try:
#         # Add a user
#         user = User(name="John 123", email="123@example.com")
#         db.add(user)
#         db.commit()
#
#         # # Query the user
#         # added_user = db.query(User).filter_by(email="johndoe@example.com").first()
#         # if added_user:
#         #     print(f"User added: {added_user.name}, {added_user.email}")
#         # else:
#         #     print("User not found")
#
#         # Query all users
#         result = db.query(User).all()
#         for r in result:
#             print(r)
#     finally:
#         db.close()

# Example usage2

class Todos:
    db = get_session()

    def add_task(self, new_task: str) -> None:
        try:
            task: TodoList = TodoList(task=new_task)
            self.db.add(task)
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def update_task(self, task_id: int, new_task: str) -> None:
        try:
            task = self.db.query(TodoList).filter_by(id=task_id).first()
            task.task = new_task
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def increment_progress(self, task_id: int) -> None:
        try:
            # if task_id > 3:
            #     raise ValueError("Task ID cannot be greater than 3")
            task = self.db.query(TodoList).filter_by(id=task_id).first()
            task.progress = task.progress + 1
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def decrement_progress(self, task_id: int) -> None:
        try:
            # if task_id < 0:
            #     raise ValueError("Task ID cannot be negative")
            task = self.db.query(TodoList).filter_by(id=task_id).first()
            task.progress = task.progress - 1
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def delete_task(self, task_id: int) -> None:
        try:
            task = self.db.query(TodoList).filter_by(id=task_id).first()
            self.db.delete(task)
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def get_all_tasks(self) -> dict:
        try:
            tasks = self.db.query(TodoList).all()
            return {
                task.id: {
                    "task": task.task,
                    "progress": task.progress
                } for task in tasks

            }
        except:
            self.db.rollback()
        finally:
            self.db.close()


if __name__ == "__main__":
    todos = Todos()

    # todos.add_task("Test this project")
    # todos.add_task("Test this project")
    # todos.add_task("Add crud operations")
    # todos.add_task("Test this project")

    # print(todos.get_all_tasks())
    # todos.increment_progress(task_id=4)
    # todos.delete_task(5)
    # print(todos.get_all_tasks())
    # todos.add_task("Fuck")
    # todos.update_task(task_id=5, new_task="Testing update")
    # print(todos.get_all_tasks())
    # db = get_session()
    #
    # try:
    #     task = TodoList(task="Finish this project")
    #
    #     db.add(task)
    #     db.commit()
    #
    #     result = db.query(TodoList).all()
    #     for r in result:
    #         print(r)
    # finally:
    #     db.close()
