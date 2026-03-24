from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pega_sessao
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos",tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Voce acessou a rota pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema,session:Session= Depends(pega_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"messagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}