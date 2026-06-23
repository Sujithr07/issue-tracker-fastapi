import json
import logging
import os
import threading
from pathlib import Path

logger = logging.getLogger(__name__)

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "issues.json"

# NOTE: This lock only serializes access within a single process (e.g. the
# default `fastapi dev` / single-worker uvicorn setup). Multi-worker or
# multi-process deployments need cross-process locking (e.g. filelock or a
# real database), which is out of scope here.
_lock = threading.Lock()


def load_data():
    """Load issues from disk. Returns [] if the file is missing, empty, or corrupt."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if not content.strip():
                return []
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                logger.error(
                    "Corrupt data file %s; treating as empty and returning []",
                    DATA_FILE,
                )
                return []
    return []


def save_data(data):
    """Persist issues to disk atomically.

    Writes to a temp file in data/ first, then os.replace() swaps it into place,
    so a crash mid-write can't leave a half-written issues.json.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with _lock:
        tmp_file = DATA_DIR / f"{DATA_FILE.name}.tmp"
        with open(tmp_file, "w") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp_file, DATA_FILE)
