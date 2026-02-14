from fastapi import FastAPI

app = FastAPI(title="MKM - Mkulukuta Moyo")

@app.get("/health")
def health():
    return {"status": "ok"}

