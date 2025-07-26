'''
Створіть власний middleware для FastAPI додатку, який буде виконувати дві основні функції: 
логування деталей запиту та перевірку наявності спеціального заголовка у запитах.

Розробіть middleware, який для кожного запиту логує таку інформацію: HTTP-метод, URL запиту, і час, коли запит був отриманий.

Виведіть інформацію у консоль сервера.

Ваш middleware повинен перевіряти, чи містить вхідний запит заголовок X-Custom-Header.

Якщо заголовок відсутній, middleware має відправляти відповідь із статус-кодом 400 (Bad Request) і повідомленням про помилку, 
не передаючи запит далі по ланцюгу обробки.

Створіть кілька тестових маршрутів у вашому FastAPI додатку, які демонструють роботу middleware.
Включіть маршрути, які відповідають звичайним запитам, а також запитам без необхідного заголовка.
'''

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()
some_text = []


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    print(f"HTTP-Method: {request.method}\nTime: {datetime.utcnow()}")
    if "X-Custom-Header" in request.headers:
        response = await call_next(request)
        return response
    return JSONResponse(status_code=400, content={"detail":"No headers"})

@app.get("/hi")
async def hi():
    return {"message":"hi"}

@app.post("/text")
async def add_some_text(text: str):
    some_text.append(text)
    return {"message":"yo"}
