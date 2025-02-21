from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/")  # Defines an API route at /. (GET request)
def read_root():  #  A function that runs when a request is made to /.
    return {"message": "Hello, FastAPI! from dev branch"}  # Return JSON response



@app.get("/users/")
def get_users():
    return [{"name": "Alice"}, {"name": "Bob"}]


# New endpoint
@app.get("/hello")
def say_hello():
    return {"message": "Hello from the dev branch!"}



























