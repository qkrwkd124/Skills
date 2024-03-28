from typing import Union

from fastapi import FastAPI, Path, Query, Body
from models import Item, User

app = FastAPI()

@app.put('/items/{item_id}')
async def update_item(
	*,
	item_id: int = Path(title='The ID of the item to get', ge=0, le=1000),
	q: str | None = None,
	item: Union[Item, None] = None,
	user : User,
	importance:int = Body(gt=0) # 단일값 gt=크거나 
):
	results = {"item_id":item_id, "user":user, "importance":importance}
	if q :
		results.update({"q":q})
	if item :
		results.update({"item":item})
	
	return results