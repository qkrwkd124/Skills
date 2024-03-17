### 쿼리 매개변수

경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언하면 "쿼리" 매개변수로 자동 해석합니다.
```python
from fastapi import FastAPI

app = FastAPI()
```

```python
fake_items_db = [{"item_name":"Foo"}, {"item_name":"Bar"},{"item_name":"Baz"}]
```
```python
@app.get("/items/")
async def read_item(skip:int=0, limit:int=10) :
	return fake_items_db[skip : skip+limit]
```

### 선택적 매개변수

```python
from typing import Union

@app.get('/items/{item_id}')
async def read_item(item_id:str, q:Union[str,None] = None) :
	if q :
		return {"item_id":item_id, "q":q}
	return {"item_id":item_id}
```
FastAPI는 `q가 = None이므로 선택적`이라는 것을 인지합니다.

### 쿼리 매개변수 형변환
```python
@app.get('/items/{item_id}')
async def read_item(item_id:str, q:Union[str,None] = None,  short:bool = False) :
	item = {"item_id":item_id}
	if q :
		item.update({"q":q})
	if not short :
		item.update({"description": "This is an amazing item that has a long description"})
	return item

```

### 필수 쿼리 매개변수
경로가 아닌 매개변수에 대한 기본값을 선언할 때(지금은 쿼리 매개변수만 보았습니다), 해당 매개변수는 필수적(Required)이지 않았습니다.  
특정값을 추가하지 않고 선택적으로 만들기 위해선 기본값을 None으로 설정하면 됩니다.  
그러나 `쿼리 매개변수를 필수로 만들려면 단순히 기본값을 선언하지 않으면` 됩니다:  

```python
@app.get("/items/{item_id}/needy")
async def read_user_item(item_id:str, needy:str):
	item = {"item_id":item_id,"needy":needy}
	return item
```

```python
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
	):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
```

 - needy, 필수적인 str.
 - skip, 기본값이 0인 int.
 - limit, 선택적인 int.