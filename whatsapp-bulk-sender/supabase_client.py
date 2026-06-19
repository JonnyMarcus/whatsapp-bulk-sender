import os
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def buscar_contatos():
    resultado = supabase.table("Contatos").select("*").limit(3).execute()
    return resultado.data

if __name__ == "__main__" :
    Contatos = buscar_contatos()
    print (Contatos)