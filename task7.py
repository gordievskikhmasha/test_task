from datetime import datetime, timedelta, timezone
import os

import jwt
from pwdlib import PasswordHash
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret") 
'''При разработке в реальном приложении 
значение секретного ключа необходимо передавать через переменную окружения. Я использую значение по умолчанию
так можно делать только для локальной разработки.'''
ALGORITHM = "HS256"

users = {} #словарь пользователей
password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    password: str


#регистрация
@app.post("/register")
def register(user: User):
    if user.username in users:
        raise HTTPException(400, "Пользователь уже существует")

    users[user.username] = password_hash.hash(user.password)

    return {"message": "Пользователь успешно зарегистрирован"}


#вход
@app.post("/login")
def login(user: User):
    hashed_password = users.get(user.username)

    if not hashed_password or not password_hash.verify(
        user.password, hashed_password
    ):
        raise HTTPException(401, "Неправильное имя пользователя или пароль")

    token = jwt.encode(
        {
            "sub": user.username,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return {"access_token": token, "token_type": "bearer"}


#проверка токена
@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        username = payload.get("sub")

        if not username or username not in users:
            raise HTTPException(401, "Invalid token")

        return {"message": "Access granted", "username": username}

    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid or expired token")
