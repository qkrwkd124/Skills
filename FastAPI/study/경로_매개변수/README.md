### 경로 매개변수

type을 지정해줄 수 있음.

```python
@app.get("/items/{item_id}")
async def read_item(item_id:int) :
	return {"item_id" : item_id}
```

### 경로 순서문제
/users/{user_id} 이전에 /users/me 를 먼저 선언해야, /users/me 요청이 제대로 작동한다.

```python
@app.get("/users/me")
async def read_user_me() :
	return {"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str) :
	return {"user_id":user_id}
```
그렇지 않으면 `/users/{user_id} 는 /users/me 요청 또한 매개변수 user_id의 값이 "me"`로 되어버린다.

### Enum 클래스 생성

Enum 클래스를 사용하면 고정된 값의 매개변수를 사용할 수 있다.
```python
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
```

### 경로를 포함하는 매개변수

```python
@app.get("/files/{file_path:path}")
async def read_file(file_path:str) :
	return {"file_path":file_path}
```
매개변수가 가져야 하는 값이 /home/johndoe/myfile.txt와 같이 슬래시로 시작(/)해야 할 수 있습니다.
이 경우 URL은: /files//home/johndoe/myfile.txt이며 files과 home 사이에 이중 슬래시(//)가 생깁니다.