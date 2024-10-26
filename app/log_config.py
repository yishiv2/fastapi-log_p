import logging
from logging.config import dictConfig
import os

def configure_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO")  # 環境変数からログレベルを取得
    
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "console": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "(%(name)s:%(lineno)d) - %(levelname)s - %(message)s",
                },
                "file": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
                },
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "level": log_level,
                    "formatter": "console",
                },
                "file": {  # ファイルハンドラー
                    "class": "logging.FileHandler",
                    "level": log_level,
                    "formatter": "file",
                    "filename": "app/log/app.log",
                    "encoding": "utf-8",
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default", "file"], "level": log_level},
                "src": {
                    "handlers": ["default", "file"],
                    "level": log_level,
                    "propagate": False,
                },
                "sqlalchemy.engine": {  # SQLAlchemyエンジンのロガー
                    "handlers": ["default", "file"],
                    "level": log_level,
                    "propagate": False,
                },
            },
        }
    )
