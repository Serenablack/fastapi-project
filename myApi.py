from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app=FastAPI()

class Task(BaseMOdel):
id:Optional[UUID]=None
title:str
description:Optional[str]=None
completed:bool=False

tasks=[]
 
@app.get("/tasks", response_model=List[Task])
def getApi():
  return tasks

  @app.post("/tasks", response_model=Task)

  def create-task(task:Task):
    task.id=uuid4()
    tasks.append(task)
    return task

if name=="__main__":
  import uvicorn
