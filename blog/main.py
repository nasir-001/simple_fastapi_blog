import email
from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic import BaseModel
from . import schemas, models
from .database import get_db, engine
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
from .routers import blog

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)


@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def getUser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not available')
    return user