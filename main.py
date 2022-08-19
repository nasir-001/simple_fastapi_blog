from typing import Optional
from fastapi import FastAPI

app = FastAPI()


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