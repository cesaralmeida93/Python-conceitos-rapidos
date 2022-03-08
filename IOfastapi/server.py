import time

import asyncio

from fastapi import FastAPI

app = FastAPI()

@app.get("/wait")
def wait():
    duration = 0.05
    time.sleep(duration)
    return {"duration": duration}


@app.get("/asyncwait")
async def asyncwait():
    duration = 0.05
    await asyncio.sleep(duration)
    return {"duration": duration}