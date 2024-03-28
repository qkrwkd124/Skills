from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() :
	return {"message": "Hello World"}


# 경로 매개변수
# type을 지정해줄 수 있음.
@app.get("/items/{item_id}")
async def read_item(item_id:int) :
	return {"item_id" : item_id}

# 경로 순서 문제
# /users/{user_id} 이전에 /users/me 를 먼저 선언해야, /users/me 요청이 제대로 작동한다.
# 그렇지 않으면 /users/{user_id} 는 /users/me 요청 또한 매개변수 user_id의 값이 "me"로 되어버린다.
@app.get("/users/me")
async def read_user_me() :
	return {"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str) :
	return {"user_id":user_id}

#Enum 클래스 생성
from enum import Enum

# string 
class ModelName(str, Enum) :
	alexnet = "alexner"
	resnet = "resnet"
	lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) :
	if model_name is ModelName.alexnet :
		return {"model_name":model_name, "message":"Deep Learning FTW!"}

	if model_name.value == "lenet" :
		return {"model_name":model_name, "message":"LeCNN all the images"}
	
	return {"model_name":model_name, "message":"Have some residuals"}


#경로를 포함하는 매개변수

@app.get("/files/{file_path:path}")
async def read_file(file_path:str) :
	return {"file_path":file_path}


#메타 데이터 선언

from typing import Union
from fastapi import Path, Query

@app.get("/items2/{item_id}")
async def read_itmes(
	*,
	item_id : int = Path(title="The ID of the item to get", ge=1),
	q: Union[str,None] = Query(default=None, alias="item-query")
):
	result = {"item_id":item_id}
	if q :
		result.update({"q":q})	
	return result

