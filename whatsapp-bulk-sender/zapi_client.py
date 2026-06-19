import os
import requests
from dotenv import load_dotenv

load_dotenv()
instance = os.getenv("ZAPI_INSTANCE")
token = os.getenv("ZAPI_TOKEN")

def enviar_mensagem(telefone,nome):
    mensagem = f"Olá, {nome} tudo bem com você?"
    url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"
    body = {"phone": telefone, "message": mensagem}
    resposta = requests.post(url, json=body)
    return resposta.json()