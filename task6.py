from pydantic import BaseModel, EmailStr, Field 
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Управление пользователями")

'''Модель данных для пользователя'''
class User(BaseModel):
    id: int
    name: str = Field(min_length=1)
    email: EmailStr

class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr

'''Хранение пользователей в памяти'''
users = []
next_id = 1

'''Создание нового пользователя'''
@app.post("/users/")
def create_user(user: UserCreate):
    global next_id
    new_user = User(
        id=next_id,
        name=user.name,
        email=user.email
    )
    users.append(new_user)
    next_id += 1
    return {"message": "Новый пользователь создан успешно",
             "user": new_user
             }

'''Просмотр всех пользователей'''
@app.get("/users/")
def get_users():
    return users 

'''Просмотр конкректного пользователя'''
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail="Пользователь не найден"
    )

'''Обновить данные о пользователе'''
@app.put("/users/{user_id}")
def update_user(user_id: int, new_user: UserCreate):
    for i, user in enumerate(users):
        if user.id == user_id:
            updated_user = User(
                id=user_id,
                name=new_user.name,
                email=new_user.email
            )
            users[i] = updated_user
            return {
                "message": "Данные пользователя обновлены",
                "user": updated_user
            }
    raise HTTPException(
        status_code=404,
        detail="Пользователь не найден"
    )

'''Удалить пользователя'''
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return {
                "message": "Пользователь удален",
                "user": deleted_user
            }
    raise HTTPException(
        status_code=404,
        detail="Пользователь не найден"
    )