from fastapi import FastAPI
from app.database.db_config import engine, Base
from app.routes import main_router
import uvicorn

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )