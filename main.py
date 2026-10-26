from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def pocetna():
    return {"poruka": "Aplikacija za trening radi!"}