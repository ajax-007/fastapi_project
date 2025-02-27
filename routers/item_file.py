from fastapi import APIRouter, FastAPI, Depends

router = APIRouter()

@router.get("/data/")
def get_data():
    return [{"name": "Laptop", "price": 1200}, {"name": "Phone", "price": 800}]

@router.post("/data/")
def create_data(item: dict):
    return {"message": "Item inserted", "item": item}


# class Route():
#     def __init__(self):
#         self.variable1 = 3
#
# router = Route()



























