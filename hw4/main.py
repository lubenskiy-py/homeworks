'''
Створіти ендпоінт API, який буде реєструвати нових користувачів, виконуючи глибоку валідацію вхідних даних.
Потрібно переконатися, що всі дані відповідають певним критеріям перед тим, як користувач буде зареєстрований.
Вимоги до валідації даних користувача:
Ім'я: мінімум 2 символи, лише літери.
Прізвище: мінімум 2 символи, лише літери.
Електронна пошта: має бути валідною електронною адресою.
Пароль: мінімум 8 символів, повинен містити хоча б одну велику літеру, одну маленьку літеру, одну цифру та один спеціальний символ.
Номер телефону: має відповідати патерну мобільного телефону.
'''

from pydantic import BaseModel, EmailStr, validator, Field
from fastapi import FastAPI, HTTPException
import re


user_list = []
app = FastAPI()


class User(BaseModel):
    id: int
    first_name: str = Field(min_length=2)
    second_name: str = Field(min_length=2)
    email: EmailStr
    password: str = Field(min_length=8)
    phone_number: str = Field(pattern=r'^\+380\d{9}$')
    # Знизу чат гєпєтє але він пояснив мені що тут і як
    @validator('password')
    def validate_password(cls, passwd):
        if not re.search('[A-Z]', passwd):
            raise HTTPException(status_code=400, detail="Password must have some capital symbol")
        if not re.search('[a-z]', passwd):
            raise HTTPException(status_code=400, detail="Password must have some small symbol")
        if not re.search(r'\d', passwd):
            raise HTTPException(status_code=400, detail="Password must have some number")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', passwd):
            raise HTTPException(status_code=400, detail="Password must have some special symbol")
        return passwd
    

@app.post("/register")
def register(user: User):
    user_list.append(user)
    return {"message":"You have successfully registered"}