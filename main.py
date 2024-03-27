from fastapi import FastAPI

app = FastAPI()

universities = ["Univeristy of Northern Iowa", "University of Iowa", "University of Iowa State"]

@app.get("/")
def read_root():
    return universities
