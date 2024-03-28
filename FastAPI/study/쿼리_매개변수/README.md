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


 ### 추가 검증

 이제 Query를 매개변수의 기본값으로 사용하여 max_length 매개변수를 50으로 설정합니다.
 min_length 설정도 가능
 ```python
 from fastapi import Query

 @app.get('/items2/')
async def read_itmes(q: Union[str,None] = Query(default=None, min_length=3, max_length=50)):
	results = {"items" :[{"item_id": "Foo"}, {"item_id":"Bar"}]}
	if q :
		results.update({"q":q})
	return results
	

 ```
 이는 데이터를 검증할 것이고, 데이터가 유효하지 않다면 명백한 오류를 보여주며, OpenAPI 스키마 경로 작동에 매개변수를 문서화 합니다.


 ### 매개변수 리스트 / 다중값

List[str]

 ```python
from typing import List
@app.get('/items3/')
async def read_items(q:Union[List[str],None] = Query(
	default=None, 
	title='Query string',
	description="lee gunhee babo",
	alias='leegunhee',
	deprecated=True
	)):
	query_items = { "q": q }
	return query_items
 ```

 List[str] 대신 list를 직접 사용할 수도 있습니다:
 이 경우 FastAPI는 리스트의 내용을 검사하지 않음을 명심하기 바랍니다.

 예를 들어, List[int]는 리스트 내용이 정수인지 검사(및 문서화)합니다. 하지만 list 단독일 경우는 아닙니다.

제네릭 검증과 메타데이터:
- alias
- title
- description
- deprecated  

특정 문자열 검증:
- min_length
- max_length
- regex
