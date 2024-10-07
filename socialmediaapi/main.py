from fastapi import FastAPI

from socialmediaapi.router.post import router

app = FastAPI()

app.include_router(router)
