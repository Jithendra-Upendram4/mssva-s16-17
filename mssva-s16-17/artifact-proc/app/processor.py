import zipfile
import json
import hashlib
import requests
from config import ENABLE_REMOTE_SCHEMA

def process_artifact(path):
    metadata = {
        "files": [],
        "checksums": {}
    }

    if path.endswith(".zip"):
        with zipfile.ZipFile(path, "r") as z:
            for name in z.namelist():
                metadata["files"].append(name)

    elif path.endswith(".json"):
        with open(path, "r") as f:
            data = json.load(f)
            metadata["files"] = list(data.keys())

    with open(path, "rb") as f:
        metadata["checksums"]["sha256"] = hashlib.sha256(f.read()).hexdigest()

    if ENABLE_REMOTE_SCHEMA:
        # Legitimate outbound request
        requests.get("https://example.com/schema")

    return metadata
