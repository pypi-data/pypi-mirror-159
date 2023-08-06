from sys import prefix
from typing import Callable
from fastapi import APIRouter, FastAPI, HTTPException, Request, Response
from fastapi.routing import APIRoute
from fastapi_filter.filter import FilterAPIRouter
from fastapi_filter.utils import loadFiltersFromFile
from starlette.middleware import Middleware
from fastapi_filter.middleware import CustomFilterMiddleware
import uvicorn


def MethodFilter(request: Request) -> Request:
    raise HTTPException(status_code=205)

router = FilterAPIRouter(prefix= "/cars").includeFilterOnMethod(method= "DoNothing", filter=MethodFilter)

middleware = [
Middleware(
    CustomFilterMiddleware, 
    filter_routers =[
        router
    ]
)
]
app = FastAPI(middleware=middleware)


@app.get("/cars/hey")
async def DoNothing():
    return "nuffin"

@app.get("/")
async def RunApp():
    return "Run"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)