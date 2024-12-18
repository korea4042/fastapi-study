from fastapi import Depends, FastAPI
# from .dependencies import get_query_token, get_token_header
from .boards.router import router

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


app.include_router(router)

        
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
