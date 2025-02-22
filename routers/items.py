from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
def get_items():
    return [{"name": "Laptop", "price": 1200}, {"name": "Phone", "price": 800}]

@router.post("/items/")
def create_item(item: dict):
    return {"message": "Item created", "item": item}































