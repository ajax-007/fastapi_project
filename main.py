from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel, Field
from routers import item_file  # Import the router

app = FastAPI()  # Create a FastAPI instance

@app.get("/")  # Defines an API route at /. (GET request)
def read_root():  #  A function that runs when a request is made to /.

    return {"message": "Hello, FastAPI! from main branch after resolving conflicts"}  # Return JSON response


@app.get("/users/")
def get_users():
    return [{"name": "Alice"}, {"name": "Bob"}]


# New endpoint
@app.get("/hello")
def say_hello():
    return {"message": "Hello from the dev branch!"}


@app.get("/xyz")
def feature_xyz():
    return {"message": "This is new feature xyz created in xyz branch"}


@app.get("/users/bill")
def get_users():
    return [{"name": "Billy"}]


@app.get("/xyz_main")
def main_xyz():
    return {"message": "This is new feature xyz created in main branch"}

# in browser we have to write:  /items/?name=Laptop&price=999.99 these are query parameters
@app.get("/items/")
def read_item(name: str, price: float):
    return {"name": name, "price": price}


class Item(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0)
    in_stock: bool


class ItemResponse(BaseModel):
    name: str
    price: float

@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    return item  # FastAPI automatically filters unwanted fields!


# Sample data storage (simulating a database)
items = {
    1: {"name": "Laptop", "price": 1200.99, "in_stock": True},
    2: {"name": "Smartphone", "price": 799.99, "in_stock": True},
}


@app.get("/item/{item_id}")     # {item_id} is a path parameter
def get_item(item_id: int):
    return {"item_id": item_id, "item": items[item_id]}


# Register the router
app.include_router(item_file.router)
# print(item_file.router.variable1)


# ---------------------------------- implementing put with path parameter ------------------------------


# Request Body Model
class ItemUpdate(BaseModel):
    name: str
    price: float
    in_stock: bool


@app.put("/items/{item_id}")  # Defines a PUT endpoint with a path parameter (item_id).
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items:
        # return {"error": "Item not found"}
        raise HTTPException(status_code=404, detail="Item not found")  # Custom error

    # Update the item
    items[item_id] = item.dict()  # Updates the item storage.
    return {"message": "Item updated", "item": items[item_id]}

# item_id: int → Extracts item_id from the URL path.
# item: ItemUpdate → Parses the request body using Pydantic.

# --------------------------------------------- delete -----------------------------------------------

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        # return {"error": "Item not found"}
        raise HTTPException(status_code=404, detail="Item not found")  # Custom error

    deleted_item = items.pop(item_id)
    return {"message": "Item deleted", "deleted_item": deleted_item}



@app.get("/abc")
def feature_abc():
    return {"message": "This is new feature abc created in main branch"}


# --------------------------------------------- dependency injection ----------------------------------------------

# Dependency function
def common_query_parameters():
    return {"q": "default", "limit": 100}

# Inject dependency
@app.get("/depends/")
def read_items(params: dict = Depends(common_query_parameters)):
    return {"parameters": params}

# ----------------------------

def pagination(limit: int = 10, offset: int = 0):
    return {"limit": limit, "offset": offset}

@app.get("/products/")
def get_products(pagination: dict = Depends(pagination)):
    return pagination

# -----------------------------

# Define the dependency
def verify_api_key(api_key: str = Header(None)):
    if api_key != "mysecretkey":  # Replace with your actual key
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/secure-data/")
def get_secure_data(api_key: str = Depends(verify_api_key)):
    return {"message": "Access granted!", "api_key": api_key}



# Test the authentication, (we can send the header through the swagger ui or other tools,
# Headers can’t be sent from the browser)











