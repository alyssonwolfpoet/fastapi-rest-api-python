```md
# 🚀 API de Pedidos com FastAPI

API REST desenvolvida com **FastAPI** para gerenciamento de usuários e pedidos, incluindo autenticação com JWT e controle de permissões (usuário e administrador).

---

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como prática de estudo baseado no curso:

- 📺 **Curso:** FastAPI - Rest API com Python  
- 📺 **Canal:** Hashtag Programação (@HashtagProgramacao)

Os testes da API foram realizados utilizando a extensão **Thunder Client** no VS Code.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Alembic (migrações)
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn

---

## 📂 Estrutura do Projeto

```

📁 app
├── main.py
├── models.py
├── schemas.py
├── auth_routes.py
├── order_routes.py
├── dependencies.py
└── banco.db

````

---

## 🔐 Autenticação

A API utiliza autenticação baseada em **JWT (JSON Web Token)**.

---

### 👤 Criar Conta

**POST** `/auth/criar_conta`

```json
{
  "nome": "Alysson",
  "email": "alysson@email.com",
  "senha": "1234abcd",
  "ativo": true,
  "admin": true
}
````

---

### 🔑 Login

**POST** `/auth/login`

```json
{
  "email": "alysson@email.com",
  "senha": "1234abcd"
}
```

**Resposta:**

```json
{
  "access_token": "token_aqui",
  "refresh_token": "token_aqui",
  "token_type": "Bearer"
}
```

---

### 🔄 Refresh Token

**GET** `/auth/refresh`

**Headers:**

```
Authorization: Bearer SEU_TOKEN
```

---

## 📦 Rotas de Pedidos

Todas as rotas abaixo exigem autenticação.

---

### 🛒 Criar Pedido

**POST** `/pedidos/pedido`

---

### ➕ Adicionar Item ao Pedido

**POST** `/pedidos/pedido/adicionar-item/{id_pedido}`

---

### ➖ Remover Item

**POST** `/pedidos/pedido/remover-item/{id_item}`

---

### ❌ Cancelar Pedido

**POST** `/pedidos/pedido/cancelar/{id_pedido}`

---

### ✅ Finalizar Pedido

**POST** `/pedidos/pedido/finalizar/{id_pedido}`

---

### 📋 Listar Todos os Pedidos (Admin)

**GET** `/pedidos/listar`

⚠️ Apenas usuários administradores podem acessar.

---

### 👤 Listar Pedidos do Usuário

**GET** `/pedidos/listar/pedidos-usuario`

---

## 🔒 Controle de Acesso

| Tipo de Usuário | Permissões                            |
| --------------- | ------------------------------------- |
| Usuário comum   | Gerencia apenas seus próprios pedidos |
| Administrador   | Acessa todos os pedidos do sistema    |

---

## ▶️ Como Executar o Projeto

### 1️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 3️⃣ Executar migrações

```bash
alembic upgrade head
```

---

### 4️⃣ Iniciar servidor

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

## 🧪 Testes

Os testes foram realizados utilizando:

* Thunder Client (VS Code)
* Requisições HTTP locais

---

## 📌 Boas Práticas Implementadas

* 🔐 Senhas armazenadas com hash (bcrypt)
* 🎟️ Autenticação com JWT
* 🔄 Uso de refresh token
* 🧱 Separação de responsabilidades (routes, models, schemas)
* 🔒 Controle de permissões (usuário vs admin)

---

## 🚀 Futuras Implementações

### 🔧 Funcionalidades

* [ ] CRUD completo de usuários
* [ ] Paginação e filtros nos pedidos
* [ ] Upload de arquivos (ex: comprovantes)
* [ ] Sistema de notificações

### 🧪 Qualidade e Testes

* [ ] Testes automatizados com Pytest
* [ ] Testes de integração
* [ ] Cobertura de código

### ⚙️ Arquitetura e Performance

* [ ] Cache com Redis
* [ ] Background tasks
* [ ] Camada de serviços (Service Layer)

### 🌐 DevOps e Deploy

* [ ] Dockerização da aplicação
* [ ] Deploy em nuvem (Render, Railway ou AWS)
* [ ] CI/CD com GitHub Actions

### 🎨 Interface

* [ ] Frontend com React ou Next.js
* [ ] Dashboard administrativo

---

## 👨‍💻 Autor

Desenvolvido por **Alysson**

```
```
