import sys
import os

base = sys.argv[1] + "/"

def pr(x, *y):
    print(x, *y)
    return x

gen_name_id = 0
def gen_name():
    global gen_name_id
    gen_name_id += 1
    return "fn" + str(gen_name_id)

gen_port_id = -1
def gen_port():
    global gen_port_id
    gen_port_id += 1
    return str(8000 + gen_port_id)


def touchdir(name):
    os.mkdir(name)
    return name

def touch(name):
    fi = open(name,"a")
    fi.write("")
    fi.close()
    return name

def scribe(name, txt):
    fi = open(name, "a")
    fi.write(txt)
    fi.close()
    return name



def id(x):
    return x

def mkdir(name):
    return lambda nxt: lambda x: nxt(touchdir(x + name + "/"))

gendir = lambda nxt: lambda x: nxt(touchdir(x + gen_name() + "/"))

def mkfile(name):
    return lambda nxt: lambda x: nxt(touch(x + name))

def text(txt):
    return lambda nxt: lambda x: nxt(scribe(x, txt))

def all(s, *v):
    if len(v) == 0:
        return s
    k = all(*v)
    return lambda nxt: s(k(nxt))

def some(*v):
    return lambda nxt: lambda x: [k(nxt)(x) for k in [*v]]

def fill_name():
    return lambda nxt: lambda x: nxt(x%(gen_name()))


rest_imports = all(text(
"""
import httpx
from fastapi import FastAPI
import json

app = FastAPI()
"""))

return_prev = all(text(
"""
    return prev
"""
))

rest_get = lambda path: all(text(
"""
@app.get("%s")
async def %s():
    stack = []
    prev = None
"""%(path, gen_name())
))

rest_post = lambda path: all(text(
"""
@app.post("%s")
async def %s(dat: dict):
    try:
        stack = []
        prev = dat
"""%(path, gen_name())
))

send_get = lambda url: all( text(
"""
        async with httpx.AsyncClient(timeout=None) as client:
            prev = await client.get("%s")
            prev = prev.json()
"""%(url)
))

send_post = lambda url, thing: all( text(
"""
        async with httpx.AsyncClient(timeout=None) as client:
            prev = await client.post("%s", data=json.dumps(%s))
            prev = prev.json()
"""%(url, thing)
))


docker_file = lambda port: all(
mkfile("Dockerfile"),
text(
"""
FROM python:latest
COPY . .
RUN pip install fastapi httpx asyncio uvicorn
EXPOSE %s
CMD ["uvicorn", "index:app", "--reload"]
"""%(port)
)
)


def rest_api(port):
    return lambda *v: all(
        mkdir(str(port)),
        some(
            docker_file(port),
            all(
                mkfile("index.py"),
                rest_imports,
                *v
            )
        )
    )

def handle_get(path):
    return lambda *v: all(rest_get(path), *v, return_prev)

def handle_post(path):
    return lambda *v: all(rest_post(path), *v, return_prev)


api_if = lambda c, t, f: text(
"""
        async with httpx.AsyncClient(timeout=None) as client:
            if %s:
                prev = await client.post("%s", data=json.dumps(prev))
            else:
                prev = await client.post("%s", data=json.dumps(prev))

            prev = prev.json()

"""%(c, t + "/post", f + "/post")
)

lh = lambda s: "http://127.0.0.1:%s"%(str(s))

label = lambda lbl: lambda *v: rest_api(lbl)(
    handle_post("/post")(all(
        *v
    )))

jmp = lambda cond, t, f: api_if(cond, lh(t), lh(f))

ret = lambda d: text(
"""
        return %s
    except:
        return {"error": ":("}
"""%(d)
)

"""
   rest_api(6969)(
        handle_get("/")(
            send_post("http://127.0.0.1:8000/post", '{"hi": "x"}')
        ),
        handle_post("/post")()
    ),
"""

inline = lambda txt: text("\t" + txt)
call = lambda lbl: send_post(lh(lbl) + "/post", "prev")
push = text(
"""
        stack.append(prev)
""")

pop = text(
"""
        prev = stack.pop()
""")

get = lambda ind: text(
"""
        prev = stack[%s]
"""%(ind))

some(
    label(8000)(
        jmp('int(prev["x"]) < 2', 8003, 8001),
        ret('prev')
    ),
    label(8001)(
       call(8002),
       push,
       call(8002),
       call(8000),
       push,
       get(0),
       call(8000),
       ret('{"x": str(int(prev["x"]) + int(stack[-1]["x"]))}')
    ),
    label(8002)(ret('{"x": str(int(prev["x"]) - 1)}')),
    label(8003)(ret('{"x": "1"}'))
)(id)(base)

