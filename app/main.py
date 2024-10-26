import logging
from fastapi import FastAPI
from app.config import get_config
from app.log_config import configure_logging  # ロギング設定をインポート

app = FastAPI()
configure_logging()


@app.on_event("startup")
async def startup_event():
    configure_logging()  # ロギング設定を初期化

@app.get("/health")
async def health_check():
    logging.getLogger("src").info("Health check endpoint called")
    return {"status": "healthy"}

