from fastapi import FastAPI

app=FastAPI()
 
@app.get("/")
def getApi():
  return {"user":"hey there"}