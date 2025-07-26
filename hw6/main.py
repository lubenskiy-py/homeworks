'''
Створіть веб-додаток на основі FastAPI, який використовує Pydantic для валідації та серіалізації даних. Додаток має включати:

Модель Користувача і Замовлення:

Користувач (User) має атрибути: ім'я, електронна пошта, список замовлень.
Замовлення (Order) має атрибути: назва продукту, кількість, ціна за одиницю.
Валідація:

Електронна пошта має бути валідною.
Назва продукту не може бути порожньою.
Кількість та ціна повинні бути позитивними числами.
Розширені Властивості:
Вкладені моделі (User замовлення як список Order).

Дефолтні значення для деяких полів (наприклад, кількість = 1).
Кастомізація серіалізації для поля з датою (наприклад, дата створення замовлення).
Маршрути API:

POST маршрут для створення нового користувача з замовленнями.
GET маршрут для отримання інформації про користувача з валідацією вхідних даних (наприклад, за електронною поштою).
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

user_list = []
app = FastAPI()


class Order(BaseModel):
    id: int
    name: str
    count: int = 1
    price: float


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    order_list: list[Order]


@app.post("/add-user")
async def add_user(user: User):
    user_list.append(user)
    return {"message":"New user added"}

@app.get("/get-user")
async def get_user(email):
    for i in user_list:
        if i.email == email:
            return {"user":i}
    raise HTTPException(status_code=404, detail="User not found")
