import logging
import os

from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Endpoints for celery worker
broker_url = os.getenv("BROKER_URL")
result_backend = os.getenv("RESULT_BACKEND")

if None in [broker_url, result_backend]:
    raise ValueError("broker url and result backend must be specified")

# Initialize the worker
try:
    from Connector import Worker

    worker = Worker.create(
        node_name="logger-producer",
        app_name="logger producer",
        worker_queue_name="logger",
        broker_url=broker_url,  # type: ignore
        result_backend=result_backend,  # type: ignore
    )
except Exception:
    logging.exception("Cannot initialize producer")
