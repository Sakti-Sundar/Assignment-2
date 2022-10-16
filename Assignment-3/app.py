from fastapi import FastAPI, APIRouter


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
   
    return ("hello world")


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="debug")