from datetime import datetime, UTC
from typing import Annotated

from fastapi import Response, Cookie, status, Header, APIRouter

from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix='/posts')

@router.get('/type/{framework}')
def read_posts(framework):
    return {'posts': [{'title': f'criando uma aplicacao com {framework}', 'author':'robson-morais', 'date': datetime.now(UTC)},
                      {'title': f'Testando a nova versão de {framework}', 'author':'robson-morais', 'date': datetime.now(UTC)}
                      ]
            }

@router.get('/type2/{framework}') #-> com tipagem nos parametros:
def read_posts2(framework: int):
    return {'posts': [{'title': f'testando {framework} como tipo', 'date': datetime.now(UTC)},
                      {'title': f'tentando {framework}', 'date': datetime.now(UTC)}
                      ]
            }

fake_db = [
    {'title': "Criando uma aplicacao com Django", 'author':'robson-morais', 'date': datetime.now(UTC), 'published':True},
    {'title': "Criando uma aplicacao com FastAPI", 'author':'robson-morais', 'date': datetime.now(UTC), 'published':True},
    {'title': "Criando uma aplicacao com Flask", 'author':'robson-morais', 'date': datetime.now(UTC), 'published':False},
    {'title': "Criando uma aplicacao com Starlett", 'author':'robson-morais', 'date': datetime.now(UTC), 'published':True}
]

# ROTAS E ENDPOINTS: QUERY PARAMETERS

@router.get("/fakedb")
def read_posts3():
    return fake_db


# skip -> quantos item pular, limit -> total de item a serem retornados a partir do skip
@router.get("/fakedb2")
def read_posts4(skip: int = 0, limit: int = len(fake_db)):
    return fake_db[skip : skip + limit]


@router.get('/fakedb3') #Adicionando a condicao booleana no parametro + lidando com Cookies
def read_posts5(response: Response, published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None, user_agent: Annotated[str | None, Header()] = None, response_model=list[PostOut]):

    response.set_cookie(key="user", value="rob.stark@dcx.com")
    print(f"Cookie: {ads_id}")

    print(f"Browser: {user_agent}")
    
    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post['published'] is published:
            posts.append(post)
    return posts



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post

