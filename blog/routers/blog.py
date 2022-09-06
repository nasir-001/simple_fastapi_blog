from fastapi import APIRouter, status, Depends, HTTPException, Response
from typing import List
from .. import schemas, models, database, oauth2
from sqlalchemy.orm import Session
from .. crud import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.get_all(db)



@router.post('/', status_code=status.HTTP_201_CREATED)
def  create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(database.get_db)):
    return blog.show(id, db)
    


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)