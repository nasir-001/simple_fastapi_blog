from fastapi import APIRouter, Depends
from blog import schemas, database
from sqlalchemy.orm import Session
from blog.crud import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)



@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)



@router.get('/{id}', response_model=schemas.ShowUser)
def getUser(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)