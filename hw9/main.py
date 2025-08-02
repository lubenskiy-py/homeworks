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

from fastapi import FastAPI, BackgroundTasks, UploadFile, HTTPException

app = FastAPI()


async def upload_photo_background(photo, photo_name):
    with open(f"./hw9/photos/{photo_name}", "wb") as p:
        p.write(photo)
    
    
@app.post("/upload-photo")
async def upload_photo(background_task: BackgroundTasks, photo: UploadFile):
    photo_type = photo.filename.split(".")
    photo_size_mb = photo.size / (1024 * 1024)
    photo_for_save = await photo.read()
    if photo_type[1] != 'png':
        raise HTTPException(status_code=400, detail="Photo must be in PNG format.")
    if len(photo_type) == 0:
        raise HTTPException(status_code=400, detail="File doesn't have a format.")
    if len(photo_type) >= 2:
        raise HTTPException(status_code=400, detail="File can't have 2 and more formats.")
    if photo_size_mb > 3:
        raise HTTPException(status_code=400, detail="Photo is too big")
    background_task.add_task(upload_photo_background, photo_for_save, photo.filename)
    return {"message":"Your photo has been saved."}
    