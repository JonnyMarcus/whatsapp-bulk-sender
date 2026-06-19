from supabase_client import buscar_contatos
from zapi_client import enviar_mensagem


if __name__ == "__main__":
    contatos = buscar_contatos()

    for contato in contatos:
        nome = contato["Nome"]
        telefone = contato["Telefone"]
        resultado = enviar_mensagem(telefone, nome)
        print(f"Enviado para {nome}: {resultado}")t 

