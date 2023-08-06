from pydantic import BaseModel as PDModel


class DbConfig(PDModel):
    host: str
    port: str
    database: str
    user: str
    password: str
    schema: str
    need_aerich: bool
