from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Nasir'}}


@app.get('/about')
def about():
    return {'data': 'About page'}
