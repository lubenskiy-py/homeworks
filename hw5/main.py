'''
Розробка API для Управління Колекцією Фільмів

Уявіть, що ви працюєте в стартапі, який створює новий стрімінговий сервіс, подібний до Netflix.
Ваша задача - розробити частину бекенду, яка відповідає за управління колекцією фільмів.
Ви вирішили використовувати FastAPI та Pydantic для створення ефективного, гнучкого та масштабованого рішення.

Створіть Pydantic модель Movie, яка має наступні поля: id (int), title (str), director (str), release_year (int), і rating (float).

API Ендпоінти:
GET /movies: Повертає список всіх фільмів.
POST /movies: Додає новий фільм до колекції.
GET /movies/{id}: Повертає інформацію про фільм за ID.
DELETE /movies/{id}: Видаляє фільм із колекції за ID.
Переконайтеся, що всі поля при додаванні нового фільму валідуються правильно. Наприклад, рік випуску не може бути у майбутньому.

Використайте Pydantic моделі для серіалізації даних фільмів у JSON, які будуть відправлені у відповідях.
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI()
movie_list = ["some element for normal using delete-movie"]


class Movie(BaseModel):
    id: int
    title: str
    director: str
    release_year: int
    rating: float


@app.get("/get-movies")
async def get_movies():
    return {"movies":movie_list}

@app.post("/add-movie")
async def add_movie(movie: Movie):
    if len(movie.title) > 50 or len(movie.title) < 1:
        raise HTTPException(status_code=400, detail="Invalid title")
    if movie.release_year < 1895 or movie.release_year > datetime.now().year:
        raise HTTPException(status_code=400, detail="Invalid year")
    if movie.rating < 0.0 or movie.rating > 10.0:
        raise HTTPException(status_code=400, detail="Invalid rating")
    movie_list.append(movie)
    return {"message":"Movie added successfully"}

@app.get("/get-movie/{id}")
async def get_movie(id: int):
    return {"movie":movie_list[id]}

@app.get("/delete-movie/{id}")
async def delete_movie(id: int):
    if id == 0:
        raise HTTPException(status_code=400, detail="No.")
    movie_list.pop(id)
    return {"movie":"movie was successfully deleted"}
