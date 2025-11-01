import asyncio
import httpx, time


async def req(client):
    start = time.time()
    # res = await client.get("http://127.0.0.1:8000/polls/hello/")
    # res = await client.get("http://127.0.0.1:8000/polls/index/")
    # res = await client.get("http://127.0.0.1:8000/polls/1/")
    res = await client.get("http://127.0.0.1:8000/polls/request_to_nbu/")
    print('res = ', res.text)
    print(f'time = {time.time() - start}')
    # return res

async def gather_tasks():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
                    req(client),
                    req(client),
                    req(client),
                    req(client),
                    req(client),
                )

asyncio.run(gather_tasks())





