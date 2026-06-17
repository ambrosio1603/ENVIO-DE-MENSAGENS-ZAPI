Envio de mensagens com Supabase + Z-API

Este projeto busca contatos no Supabase e envia uma mensagem personalizada via Z-API.

---

Setup no Supabase

1. Faça login no [Supabase](https://supabase.com) e acesse seu projeto.
2. No menu lateral, clique em **"Table Editor"**.
3. Clique em **"Create a new table"** e preencha:
   - **Name**: `contacts`
   - **Enable Row Level Security (RLS)**: Desligado (para testes).
4. Adicione as seguintes colunas (além do `id` que já vem padrão):
   - Clique em **"Add Column"**:
     - **Name**: `name` | **Type**: `text` | **Default**: vazio
   - Clique em **"Add Column"** novamente:
     - **Name**: `phone` | **Type**: `text` | **Default**: vazio
5. Clique em **"Save"** para criar a tabela.
6. Vá na aba **"Insert"** e adicione alguns contatos de exemplo:
   - Exemplo: `name` = `João Silva`, `phone` = `5511999991111` (formato: DDI + DDD + Número, sem espaços).



Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-anon-public
ZAPI_INSTANCE_ID=seu-instance-id
ZAPI_API_TOKEN=seu-token
ZAPI_API_URL=https://api.z-api.io

\## Como rodar



1\. Clone o repositório

2\. Crie um ambiente virtual: `python -m venv venv`

3\. Ative: `venv\\Scripts\\activate` (Windows)

4\. Instale as dependências: `pip install -r requirements.txt`

5\. Crie um arquivo `.env` com suas credenciais (veja o `.env.example`)

6\. Execute: `python main.py`



\## Tecnologias

\- Python

\- Supabase (banco de dados)

\- Z-API (envio de WhatsApp)

