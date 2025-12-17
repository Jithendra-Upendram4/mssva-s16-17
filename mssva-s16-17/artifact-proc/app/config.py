import os

PROCESSOR_MODE = os.getenv("PROCESSOR_MODE", "normal")
ENABLE_REMOTE_SCHEMA = os.getenv("ENABLE_REMOTE_SCHEMA", "false").lower() == "true"
