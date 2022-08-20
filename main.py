from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# models
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

@app.get('/blogs')
def index(published: bool = True, limit: int = 10, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from database'}
    else:
        return {'data': f'{limit} blogs from database'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def singleBlog(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2'}}



@app.post('/blog')
def create(blog: Blog):
    # return {'data': 'blog is successfully created'}
    return blog