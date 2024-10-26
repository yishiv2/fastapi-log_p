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
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "level": log_level,
                    "formatter": "console",
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default"], "level": log_level},
                "src": {
                    "handlers": ["default"],
                    "level": log_level,
                    "propagate": False,
                },
                "sqlalchemy.engine": {  # SQLAlchemyエンジンのロガー
                    "handlers": ["default"],
                    "level": log_level,  # 環境変数から取得したログレベルを設定
                    "propagate": False,
                },
            },
        }
    )
