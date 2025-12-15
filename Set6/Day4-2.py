import logging

# -----------------------------------------
# 1. Color settings (ANSI escape codes)
# -----------------------------------------
RESET = "\033[0m"
COLORS = {
    "DEBUG": "\033[94m",     # Blue
    "INFO": "\033[92m",      # Green
    "WARNING": "\033[93m",   # Yellow
    "ERROR": "\033[91m",     # Red
    "CRITICAL": "\033[95m",  # Magenta
}

# -----------------------------------------
# 2. Custom Formatter with Colors
# -----------------------------------------
class ColorFormatter(logging.Formatter):
    def format(self, record):
        log_color = COLORS.get(record.levelname, RESET)
        message = super().format(record)
        return f"{log_color}{message}{RESET}"

# -----------------------------------------
# 3. Configure logging
# -----------------------------------------
def setup_logger():
    handler = logging.FileHandler("test.txt","a")
   
    formatter = ColorFormatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    handler.setLevel(logging.ERROR)
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    logger.propagate = False   # avoid duplicate logs

    return logger

# Create the logger once
logger = setup_logger()

def display():
    logger.debug("This is a debug message")
    logger.info("Everything looks good!")
    logger.warning("This is a warning")
    logger.error("An error occurred!")
    logger.critical("Critical issue!")

display()