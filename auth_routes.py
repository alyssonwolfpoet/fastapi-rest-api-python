from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pega_sessao
from main import bcrypt_context
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth",tags=["auth"])

def criar_token(id_usuario):
    token = f"kahfhksahgala{id_usuario}"
    return token

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"mensagem": "Voce acessou a rota order","autenticado": False}

@auth_router.post("/criar_conta")
async def Criar_conta(usuario_schema: UsuarioSchema,session:Session= Depends(pega_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        # ja existe um usuario com esse email
        raise HTTPException(status_code=400,detail="e-mail do usuario ja cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome,usuario_schema.email, senha_criptografada,usuario_schema.ativo,usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"usuario cadastrado com sucesso {usuario_schema.email}"}
    
# login -> email e senha -> jwt (json web token) ilauhfwkkhfkwahfwçofwçoehifçowfowifpowi

@auth_router.post("/login")
async def login(login_schema: LoginSchema ,session: Session = Depends(pega_sessao) ):
    usuario = session.query(Usuario).filter(Usuario.email==login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=400,detail="Usuario não encontrado")
    else:
        acess_token = criar_token(usuario.id)
        return {
            "acess_token": acess_token,
            "token_type": "Bearer"
        }
        # JWT Bearer

        #h eader =  {"Access-token: Bearer token"}