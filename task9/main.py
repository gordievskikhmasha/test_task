from fastapi import FastAPI, Header, HTTPException
import subprocess

app = FastAPI()

@app.post("/")
def hello(test: str | None = Header(default=None)):
    if test != "Hello":
        raise HTTPException(status_code=403, detail="Forbidden")

    return "Hello, World!"

@app.get("/health")
def health():
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2", "77.88.8.8"],
            capture_output=True,
            timeout=3,
        )

        if result.returncode == 0:
            return "OK"

        raise HTTPException(status_code=503, detail="Ping failed")

    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=503, detail="Ping timeout")
