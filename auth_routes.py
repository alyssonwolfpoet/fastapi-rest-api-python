from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pega_sessao
from main import bcrypt_context

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
        raise HTTPException(status_code=400,detail="e-mail do usuario ja cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome,email,senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuario cadastrado com sucesso"}