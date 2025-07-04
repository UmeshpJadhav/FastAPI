from fastapi import FastAPI

app = FastAPI()

#with the help of decorator we create the route
@app.get("/")
def hello():
    return{'message':'Hello world'}

@app.get("/about")
def about():
    return{'message':'campus x bro'}