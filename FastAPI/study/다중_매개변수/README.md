### 다중 본문 매개변수
### 중첩모델
```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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

class User(BaseModel) :
	username:str
	full_name: Union[str,None] = None

@app.put('/items/{item_id}')
async def update_item(
	*,
	item_id: int = Path(title='The ID of the item to get', ge=0, le=1000),
	q: str | None = None,
	item: Union[Item, None] = None,
	user : User,
	importance:int = Body(gt=0) # 단일값
):
	results = {"item_id":item_id, "user":user, "importance":importance}
	if q :
		results.update({"q":q})
	if item :
		results.update({"item":item})
	
	return results
```
Body 또한 Query, Path 그리고 이후에 볼 다른 것들처럼 동일한 추가 검증과 메타데이터 매개변수를 갖고 있습니다.

아래와 같은 이점을 제공한다.

- 편집기 지원 (자동완성이 어디서나!)
- 데이터 변환 (일명 파싱/직렬화)
- 데이터 검증
- 스키마 문서화
- 자동 문서