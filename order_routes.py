from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from dependencies import pega_sessao, verificar_token
from schemas import PedidoSchema
from models import Pedido, Usuario

order_router = APIRouter(prefix="/pedidos",tags=["pedidos"],dependencies= [Depends(verificar_token)])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Voce acessou a rota pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema,session:Session= Depends(pega_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"messagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}

@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int,session:Session= Depends(pega_sessao),usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=400, detail="Você não tem autorização para fazer essa modificação")
    pedido.status = "CANCELADO"
    session.commit()
    return{
        "mensagem": f"Pedido número : {pedido.id} cancelado com sucesso",
        "pedido": pedido
    }
