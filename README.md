# WhatsApp Bulk Sender

Script em Python para consultar contatos no Supabase e enviar mensagens por meio da Z-API.

> **Segurança:** credenciais que já apareceram em versões públicas devem ser revogadas e substituídas. O exemplo abaixo contém apenas placeholders. Use este projeto somente com contatos que autorizaram o recebimento de mensagens e respeite os termos dos provedores.

## Estado atual

O código consulta até três registros da tabela `Contatos` e envia uma mensagem por contato. Não há testes automatizados, tratamento de timeout/retries, validação do conteúdo dos registros nem confirmação de consentimento implementados. A execução real depende de credenciais e serviços externos; não foi validada nesta auditoria.

## Requisitos

- Python 3
- Uma instância Supabase com a tabela `Contatos`
- Uma instância Z-API configurada

## Execução

A partir da pasta `whatsapp-bulk-sender`:

```bash
python -m venv .venv
# Ative o ambiente virtual
pip install -r requirements.txt
```

Copie `.env.example` para `.env` e preencha os valores localmente. Não envie `.env` ao Git.

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=replace-with-a-rotated-supabase-key
ZAPI_INSTANCE=replace-with-instance-id
ZAPI_TOKEN=replace-with-z-api-token
```

Execute com:

```bash
python main.py
```

## Limitações e próximos passos

- Rotacionar qualquer credencial já publicada e revisar o histórico público do repositório.
- Validar variáveis obrigatórias antes de criar clientes.
- Adicionar timeout, tratamento de respostas HTTP e logs sem dados pessoais.
- Validar telefone e consentimento antes do envio; adicionar modo de simulação.
- Criar testes unitários com chamadas HTTP e Supabase simuladas.

## Licença

Nenhuma licença foi identificada neste repositório.