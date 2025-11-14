from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categora',max_length=10)] #como seria usar o parametro 'examples' aqui?