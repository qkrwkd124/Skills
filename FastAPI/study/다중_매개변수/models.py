from pydantic import BaseModel, Field, HttpUrl
from typing import Union, Set, List

class Image(BaseModel) :
	url : HttpUrl
	name : str

class Item(BaseModel) :
	name: str = Field(default="younpark", description="윤팍의모험")
	description: str | None = None
	price: float
	tax: float | None = None
	tags: Set[str] = set()
	image : Union[List[Image], None] = None

	#에제 데이터 선언
	model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

class User(BaseModel) :
	username:str
	full_name: Union[str,None] = None