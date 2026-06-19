# 📲 WhatsApp Bulk Sender

Projeto desenvolvido em **Python** que lê contatos cadastrados em um banco de dados no **Supabase** e envia mensagens personalizadas via **WhatsApp** utilizando a **Z-API**.

## 🚀 Funcionalidades

- Leitura de contatos direto do banco de dados (Supabase)
- Envio de mensagens personalizadas via WhatsApp (Z-API)
- Suporte para até 3 contatos por execução
- Credenciais protegidas com variáveis de ambiente (.env)

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Supabase (banco de dados)
- Z-API (envio de mensagens WhatsApp)
- python-dotenv
- requests

---

## 📂 Estrutura do Projeto

```text
whatsapp-bulk-sender/
├── main.py              → ponto de entrada
├── supabase_client.py   → conexão e busca no banco
├── zapi_client.py       → envio de mensagens via Z-API
├── requirements.txt     → dependências do projeto
├── .env                 → credenciais (não sobe pro GitHub)
└── .gitignore
```

---

## ⚙️ Como Configurar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/whatsapp-bulk-sender.git
cd whatsapp-bulk-sender
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o `.env`

Crie um arquivo `.env` na raiz do projeto:
SUPABASE_URL=https://lxgqndfbsvqewpeupsqi.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx4Z3FuZGZic3ZxZXdwZXVwc3FpIiwicm9sZSI6ImiLCJpYXQiOjE3ODE4Nzk0MjEsImV4cCI6MjA5NzQ1NTQyMX0.5BpQ_hxAGsBV44tfTGjupnjgDZqHE6bhKmXE0PC_jbg
ZAPI_INSTANCE=3F4E331C58C691F68467CE717FF40C71
ZAPI_TOKEN=C94EE2C2DC8FCC1CFAC81F2A

### 4. Configure o Supabase

Crie uma tabela chamada `Contatos` com as colunas:

- `id` (int, primary key)
- `Nome` (text)
- `Telefone` (text) — formato: `5511999999999`

### 5. Conecte o WhatsApp na Z-API

Acesse [z-api.io](https://z-api.io), crie uma instância e conecte seu WhatsApp pelo QR Code.

---

## ▶️ Como Executar

```bash
python main.py
```

---

## 👨‍💻 Autor

**Jonny Marcus**

Estudante de Ciência da Computação apaixonado por automação, desenvolvimento de software e soluções práticas.
