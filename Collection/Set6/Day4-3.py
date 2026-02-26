# your_project/
# ├─ logging_config/
# │  ├─ __init__.py
# │  ├─ config.py          # central dictConfig + initializer
# │  ├─ factory.py         # get_logger(...) wrapper
# │  └─ logging.yaml       # optional: external config
# ├─ tests_ui/
# │  └─ ui_test.py
# ├─ api/
# │  └─ service.py
# └─ main.py               # app entry: initializes logging

# logging_config/config.py
import logging
import logging.config
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = os.environ.get("LOG_DIR", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

DEFAULT_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")

BASE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
DATEFMT = "%Y-%m-%d %H:%M:%S"

def get_default_config(app_name="app"):
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": BASE_FORMAT,
                "datefmt": DATEFMT
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "stream": "ext://sys.stdout"
            },
            "rotating_file_app": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filename": os.path.join(LOG_DIR, f"{app_name}.log"),
                "maxBytes": 10 * 1024 * 1024,
                "backupCount": 5,
                "encoding": "utf8"
            }
        },
        "loggers": {
            # root-like app logger
            app_name: {
                "handlers": ["console", "rotating_file_app"],
                "level": DEFAULT_LEVEL,
                "propagate": False
            }
        },
        "root": {
            "handlers": ["console", "rotating_file_app"],
            "level": DEFAULT_LEVEL
        }
    }

def init_logging(app_name="app", extra_loggers: dict | None = None):
    """
    Initialize logging once (call from app entrypoint).
    extra_loggers: mapping logger_name -> dict like {"handlers": [...], "level": "..."} to add per-component rules.
    """
    cfg = get_default_config(app_name=app_name)
    if extra_loggers:
        cfg["loggers"].update(extra_loggers)
    logging.config.dictConfig(cfg)


# logging_config/factory.py
import logging

def get_logger(name: str, component: str | None = None, level: str | None = None):
    """
    name: typically __name__ in callers
    component: optional short logical name -> e.g., "ui", "api", "mobile"
    level: optional override ("DEBUG","INFO", etc.)
    """
    logger_name = f"{component}.{name}" if component else name
    logger = logging.getLogger(logger_name)
    if level:
        logger.setLevel(level)
    return logger

# main.py
from logging_config.config import init_logging
from logging_config.factory import get_logger

if __name__ == "__main__":
    # initialize once at process startup
    init_logging(app_name="my_test_app", extra_loggers={
        "ui": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "api": {"handlers": ["console"], "level": "INFO", "propagate": False},
    })

    logger = get_logger(__name__, component="app")
    logger.info("Application started")

# api/service.py
from logging_config.factory import get_logger

logger = get_logger(__name__, component="api")

def call_backend():
    logger.info("Calling backend endpoint /health")
    # ...
    logger.error("Backend returned 500")

# Per-component files (optional)

"handlers": {
    "rotating_file_ui": {..., "filename": os.path.join(LOG_DIR,"ui.log")},
    "rotating_file_api": {..., "filename": os.path.join(LOG_DIR,"api.log")},
    ...
},
"loggers": {
    "ui": {"handlers": ["console","rotating_file_ui"], "level": "DEBUG", "propagate": False},
    "api": {"handlers": ["console","rotating_file_api"], "level": "INFO", "propagate": False},
}


# YAML alternative (if you prefer file-based config)

version: 1
disable_existing_loggers: false
formatters:
  standard:
    format: '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: standard
    stream: ext://sys.stdout
  ui_file:
    class: logging.handlers.RotatingFileHandler
    formatter: standard
    filename: logs/ui.log
    maxBytes: 10485760
    backupCount: 5
loggers:
  ui:
    handlers: [console, ui_file]
    level: DEBUG
    propagate: false
root:
  handlers: [console]
  level: INFO

# Best Practices

# Initialize once at program entry. Don’t call basicConfig in libraries — configure in your app/test runner.

# Use named loggers (get_logger(__name__, component=...)) so logs show module path.

# Use RotatingFileHandler to avoid huge logs.

# For tests, you may set LOG_LEVEL=DEBUG via env var.

# Keep propagate=False for component-specific file handlers to avoid duplicate logs.

# Use structured logging (JSON formatter) if logs will be consumed by log aggregators.

# Avoid creating handlers repeatedly — configure centrally and reuse.