from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from dependencies import pega_sessao, verificar_token
from schemas import PedidoSchema , ItemPedidoSchema
from models import Pedido, Usuario,ItensPedido

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


@order_router.get("/listar")
async def listar_pedidos(session:Session= Depends(pega_sessao),usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=400,detail="Voce nao tem autorização pra fazer essa operaçao")
    else:
        pedidos = session.query(Pedido).all()
        return {
            "pedidos" : pedidos
        }
        
@order_router.post("/pedido/adicionar-item/{id_pedido}")
async def adicionar_item_pedido(id_pedido:int ,
                                item_pedido_schema: ItemPedidoSchema,
                                session:Session= Depends(pega_sessao),
                                usuario: Usuario = Depends(verificar_token)):


    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400,detail="pedido inexistente")
    if not usuario.admin and usuario.id != pedido.id:
        raise HTTPException(status_code=401,detail=" voçê não tem autorização pra essa operação")
    
    item_pedido = ItensPedido(item_pedido_schema.quantidade,
                              item_pedido_schema.sabor,
                              item_pedido_schema.tamanho,
                              item_pedido_schema.preco_unitario,
                              id_pedido
                              )
    
    session.add(item_pedido)
    pedido.calcular_preco()
    session.commit()
    return {
        "messagem" : "item criado com sucesso",
        "item_id": item_pedido.id,
        "preco_pedido": pedido.preco
    }
    
    
@order_router.post("/pedido/remover-item/{id__item_pedido}")
async def remover_item_pedido(id_item_pedido:int,
                                session:Session= Depends(pega_sessao),
                                usuario: Usuario = Depends(verificar_token)):


    item_pedido = session.query(ItensPedido).filter(ItensPedido.id==id_item_pedido).first()
    pedido = session.query(Pedido).filter(Pedido.id==item_pedido.pedido).first()
    if not item_pedido:
        raise HTTPException(status_code=400,detail="Item no pedido inexistente")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401,detail=" voçê não tem autorização pra essa operação")
    
    session.delete(item_pedido)
    pedido.calcular_preco()
    session.commit()
    return {
        "messagem" : "item removido com sucesso",
        "quantidade_itens_pedido": len(pedido.itens),
        "pedido":  pedido
    }    