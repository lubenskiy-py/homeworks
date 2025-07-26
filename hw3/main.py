'''
Організація простої системи управління завданнями (To-Do List)

Мета завдання: створити веб-застосунок на основі FastAPI, який дозволяє користувачеві керувати своїм списком завдань.

Функціональні вимоги до системи:

- Додавання нового завдання.
- Редагування існуючого завдання.
- Видалення завдання.
- Отримання інформації про конкретне завдання за його ідентифікатором.
- Відображення всіх завдань.

Технічні деталі завдання:
- Використовуйте різні HTTP-методи (GET, POST, PUT, DELETE) для реалізації різних функцій.
- Використовуйте шляхові параметри для ідентифікації конкретних завдань.
- Переконайтеся, що ви використовуєте валідацію вхідних даних, де це потрібно.
'''

from fastapi import FastAPI

to_do_dict = dict()
app = FastAPI()


@app.post("/add-task")
def add_task(id: int, task: str):
    to_do_dict[id] = task
    return {"message":"Your task has been added"}


@app.put("/completely-editing-task")
def completely_editing_task(id: int, edited_task: str):
    to_do_dict[id] = edited_task
    return {"message":"Your task has been edited"}


@app.delete("/delete-task")
def delete_task(id: int):
    del to_do_dict[id]
    return {"message":"Your task has been deleted"}


@app.get("/get-task/{id}")
def get_task(id: int):
    return to_do_dict[id]


@app.get("/get-all-tasks")
def get_all_tasks():
    return to_do_dict
