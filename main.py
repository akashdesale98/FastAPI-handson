from os import name
from typing import Optional
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from starlette.routing import Host 
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return { 'data' : f'{limit} published blogs from the db' }    
    return { 'data' : f'{limit} blogs from the db' }

@app.get('/blog/unpublished')
def getUnpublieshed():
    return { 'data' : 'unpublished blog'}

@app.get('/blog/{id}')
def getBlog(id: int):
    return { 'data' : id}

@app.get('/blog/{id}/comments')
def getComments(id, limit=10):
    return limit
    # return { "data" : id }

class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool]

@app.post('/blog')
def createBlog(blog: Blog):
    return {'data' : f'Blog with the title {blog.title} has been created'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)