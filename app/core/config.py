import os
from dotenv import load_dotenv

# Loads .env locally, ignored in production
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")
