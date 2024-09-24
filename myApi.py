from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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
  for task in tasks:
    if task.id==task_id: 
      return task

  return HTTPException(status_code=404, detail="task not found")

@app.put("/tasks/{task_id}", response_model=Task)

def update_task(task_id:UUID, task_update:Task ):
  for idx, task in enumerate(tasks):
    if task.id==task_id:
      updated_task=task.copy(update=task_update.dict(exclude_unset=true))
      tasks[idx]=updated_task
      return updated_task
  return HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id:UUID):
  task.pop(task_id) return HTTPException(status_code=404, detail="task not found")
return tasks



if __name__=="__main__":
  import uvicorn



