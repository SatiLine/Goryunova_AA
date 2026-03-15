from fastapi import APIRouter, HTTPException, Path, Query
from pydantic import BaseModel, Field
import logging  

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

router = APIRouter(prefix="/items", tags=["items"])

fake_db = {1: {"name": "Foo", "price": 50.2}}

class Item(BaseModel):
    name: str = Field(..., title="Название", example="Телефон")
    price: float = Field(..., gt=0, title="Цена", example=199.99)
    is_offer: bool | None = Field(None, title="Акционный товар")

@router.get("/{item_id}")
def read_item(
    item_id: int = Path(..., title="ID товара", ge=1),
    q: str | None = Query(None, title="Поисковый запрос", max_length=50)
):
    logger.info(f"Запрос товара с id={item_id}")  
    if item_id not in fake_db:
        logger.warning(f"Товар с id={item_id} не найден")  
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": fake_db[item_id], "q": q}

@router.post("/")
def create_item(item: Item):
    for existing_item in fake_db.values():
        if existing_item["name"] == item.name:
            logger.warning(f"Попытка создать дубликат: {item.name}")  
            raise HTTPException(
                status_code=400,
                detail=f"Товар с именем '{item.name}' уже существует"
            )
    new_id = max(fake_db.keys()) + 1
    fake_db[new_id] = {"name": item.name, "price": item.price}
    logger.info(f"Создан новый товар: {item.name}, id={new_id}")  
    return item

@router.put("/{item_id}")
def update_item(
    item_id: int = Path(..., title="ID товара", ge=1),
    item: Item = ...,
):
    logger.info(f"Обновление товара с id={item_id}") 
    if item_id not in fake_db:
        logger.warning(f"Товар с id={item_id} не найден для обновления")  
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = {"name": item.name, "price": item.price}
    return {"item_id": item_id, "updated_item": fake_db[item_id]}

