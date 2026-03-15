from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pega_sessao

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"mensagem": "Voce acessou a rota order","autenticado": False}

@auth_router.post("/criar_conta")
async def Criar_conta(email: str, senha: str,nome:str,session= Depends(pega_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        # ja existe um usuario com esse email
        return {"mensagem": "ja exite um usuario com esse email"}
    else:
        novo_usuario = Usuario(nome,email,senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuario cadastrado com sucesso"}