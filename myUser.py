
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional
from uuid import UUID, uuid4class User(BaseModel):
  user: str
  email:str|None=None
  full_name:str|None=None
  disabled:bool:None=None
  users=[]