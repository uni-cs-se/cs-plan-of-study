from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def fn1():
    print("get")
    return {"yay": ":)"}


@app.post("/post")
def fn2(s: dict):
    print(s)
    return s

