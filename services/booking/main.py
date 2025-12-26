from fastapi import FastAPI
from database import get_db_connection

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "booking service running"}

@app.get("/db-health")
def db_health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "detail": str(e)}

