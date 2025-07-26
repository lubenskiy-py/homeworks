'''
Як розробники мистецького порталу, ваше завдання — створити API для фото-галереї, яке дозволяє художникам завантажувати, зберігати та обробляти свої твори.

Ендпоінт має приймати одне або кілька зображень від користувачів.
Використайте мультипарт-форму для прийому файлів.
Реалізуйте логіку для перевірки формату (наприклад, JPG, PNG) та розміру зображень.
Відхиліть файли, які не відповідають визначеним критеріям.
Розробіть механізм для зберігання завантажених файлів у локальній файловій системі або обраному хмарному сховищі.
Використайте фонові завдання для оптимізації зображень (наприклад, зменшення розміру, конвертація формату).
Забезпечте асинхронну обробку, щоб не блокувати основний потік запитів.
Напишіть тести для перевірки функціоналу завантаження, валідації та зберігання файлів.
Переконайтеся, що фонові завдання працюють коректно.
Імплементуйте механізми для санітізації та безпечного оброблення завантажених файлів.
Застосуйте найкращі практики для захисту збережених файлів та доступу до них.
'''

from fastapi import FastAPI, BackgroundTasks, UploadFile, File
import os
import shutil
from PIL import Image

app = FastAPI()


def upload_photo_background(photo, photo_name, photo_size):
    photo_type = photo_name.split(".")
    photo_size_mb = photo_size / (1024 * 1024)

    if photo_type[1] == None:
        return {"message":"File dont have a format."}
    
    if photo_type[2] != None:
        return {"message":"File cant have 2 and more formats."}
    
    if photo_type[1] != 'png':
        return {"message":"Photo must be in PNG format."}
    
    if photo_size_mb > 3:
        return {"message":"Photo is too big"}
    
    with open(f"./photos/{photo_name}", "wb") as p:
        shutil.copyfileobj(photo, p)

    return {"message":"Your photo has been upload."}
    
    
@app.post("/upload-photo")
async def upload_photo(background_task: BackgroundTasks, photo: UploadFile):
    background_task.add_task(upload_photo_background, photo.file, photo.filename, photo.size)
    return {"message":"Your photo has been sent for verification."}
    