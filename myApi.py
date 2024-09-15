from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app=FastAPI()

class Task(BaseModel):
  id:Optional[UUID]=None
  title:str
  description:Optional[str]=None
  completed:bool=False

tasks=[]
 
@app.get("/tasks", response_model=List[Task])
def getApi():
  return tasks

@app.post("/tasks", response_model=Task)

def create_task(task:Task):
    task.id=uuid4()
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}",response_model=Task)
def getOneApi(task_id:UUID):
fortask in tasks:
  if task.id==task_id
  return task
@app.put("/tasks", response_model=Task)

def update_task(task:Task)
tasks.append(task)
return task

if __name__=="__main__":
  import uvicorn



