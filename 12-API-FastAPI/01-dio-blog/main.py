from datetime import datetime, UTC

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

@app.get('/posts/type/{framework}')
def read_posts(framework):
    return {'posts': [{'title': f'criando uma aplicacao com {framework}', 'date': datetime.now(UTC)},
                      {'title': f'Testando a nova versão de {framework}', 'date': datetime.now(UTC)}
                      ]
            }

@app.get('/posts/type2/{framework}') #-> com tipagem nos parametros:
def read_posts2(framework: int):
    return {'posts': [{'title': f'testando {framework} como tipo', 'date': datetime.now(UTC)},
                      {'title': f'tentando {framework}', 'date': datetime.now(UTC)}
                      ]
            }

# ROTAS E ENDPOINTS: QUERY PARAMETERS

fake_db = [
    {'title': "Criando uma aplicacao com Django", 'date': datetime.now(UTC)},
    {'title': "Criando uma aplicacao com FastAPI", 'date': datetime.now(UTC)},
    {'title': "Criando uma aplicacao com Flask", 'date': datetime.now(UTC)},
    {'title': "Criando uma aplicacao com Starlett", 'date': datetime.now(UTC)}
]

@app.get("/posts/fakedb")
def read_posts3():
    return fake_db

# skip -> quantos item pular, limit -> total de item a serem retornados a partir do skip
@app.get("/posts/fakedb2")
def read_posts4(skip: int = 0, limit: int = len(fake_db)):
    return fake_db[skip : skip + limit]

fake_db2 = [
    {'title': "Criando uma aplicacao com Django", 'date': datetime.now(UTC), 'published':True},
    {'title': "Criando uma aplicacao com FastAPI", 'date': datetime.now(UTC), 'published':True},
    {'title': "Criando uma aplicacao com Flask", 'date': datetime.now(UTC), 'published':False},
    {'title': "Criando uma aplicacao com Starlett", 'date': datetime.now(UTC), 'published':True}
]

@app.get('/posts/fakedb3') #Adicionando a condicao booleana no parametro; se ela é obrigatoria para esta funcao, entao ela antecede os outros parametros
def read_posts5(published: bool, limit: int, skip: int = 0):
    posts = []
    for post in fake_db2:
        if len(posts) == limit:
            break
        if post['published'] is published:
            posts.append(post)
    return posts

 
# REQUEST BODY
class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False


@app.post('/posts/', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db2.append(post.model_dump())
    return post

