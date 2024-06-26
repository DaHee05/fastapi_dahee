from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from comment import comment_router # added
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5538", "http://34.201.238.254:8086"]
#origins = ["http://127.0.0.1:5538", "http://50.17.29.177/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def welcome() -> dict:
    return {
        "msg" : "hello world?"
    }

app.include_router(comment_router)  # added

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)


#d
