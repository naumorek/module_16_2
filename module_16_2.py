from typing import Annotated

from fastapi import FastAPI,Path

# Создаем экземпляр приложения FastAPI uvicorn module_16_1:app --reload
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def root():
    return {"Главная страница"}



@app.get("/user/{username}/{age}")
async def read_username_age(
        username: Annotated[str,Path(min_lenght=5,max_length=20,description="Enter username", examples="Andrey")],
        age:Annotated[int,Path(ge=18,le=120,description="Enter age", examples="33")]):
    return {"messege": f"{username},{age}"}

@app.get("/user/admin")
async def id_admin():
    return {"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def id_user(user_id:Annotated[int,Path(ge=1,le=100,description="Enter userID", examples="1")]):
    return {f"Вы вошли как пользователь № {user_id}"}


