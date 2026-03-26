from fastapi import Depends, HTTPException
from main import SECRETE_KEY, ALGORITH, Oauth2_schema
from models import db
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario
from jose import jwt, JWTError


def pega_sessao():
    try:
        Session = sessionmaker(bind=db) 
        session = Session()
        yield session
    finally:
        session.close

def verificar_token(token: str = Depends(Oauth2_schema), session: Session = Depends(pega_sessao)):
    try:
        dic_info = jwt.decode(token, SECRETE_KEY, ALGORITH)
        id_usuario= int(dic_info.get("sub"))
    except JWTError as erro:
        print(erro)
        raise HTTPException(status_code=401,detail="Acesso negado, verifique a validade do token")
    # verificar se o token é valido
    # extrair o id do usuario do token
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401,detail="Acesso invalido")
    return usuario