from fastapi import FastAPI

app = FastAPI()


fake_items_db = [{"item_name":"Foo"}, {"item_name":"Bar"},{"item_name":"Baz"}]

@app.get("/items/")
async def read_item(skip:int=0, limit:int=10) :
	return fake_items_db[skip : skip+limit]


#선택적 매개변수
from typing import Union

# @app.get('/items/{item_id}')
# async def read_item(item_id:str, q:Union[str,None] = None) :
# 	if q :
# 		return {"item_id":item_id, "q":q}
# 	return {"item_id":item_id}

#쿼리 매개변수 형변환
@app.get('/items/{item_id}')
async def read_item(item_id:str, q:Union[str,None] = None,  short:bool = False) :
	item = {"item_id":item_id}
	if q :
		item.update({"q":q})
	if not short :
		item.update({"description": "This is an amazing item that has a long description"})
	return item

#필수 쿼리매개변수

@app.get("/items/{item_id}/needy")
async def read_user_item(item_id:str, needy:str):
	item = {"item_id":item_id,"needy":needy}
	return item
	
@app.get("/needy")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
	):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


# 추가 검증
from fastapi import Query

@app.get('/items2/')
async def read_itmes(q: Union[str,None] = Query(default=None, min_length=3, max_length=50)):
	results = {"items" :[{"item_id": "Foo"}, {"item_id":"Bar"}]}
	if q :
		results.update({"q":q})
	return results


# 매개변수 리스트 / 다중값

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

