import httpx
import asyncio
import json

url = "http://127.0.0.1:8000"

async def main():
    async with httpx.AsyncClient(timeout=None) as client:
        #get = await client.get(url)
        #print(get)

        post = await client.post(url + "/post", data=json.dumps({"x": 

                                                                input("input n: "), "y": "aww"}))
        print(post.json()["x"])

asyncio.run(main())
