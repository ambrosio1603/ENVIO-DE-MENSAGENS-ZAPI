import os
import logging
from dotenv import load_dotenv
from supabase import create_client, Client
import requests

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_API_TOKEN = os.getenv("ZAPI_API_TOKEN")
ZAPI_API_URL = os.getenv("ZAPI_API_URL", "https://api.z-api.io")

def fetch_contacts(limit=3):
    try:
        response = supabase.table("contacts").select("*").limit(limit).execute()
        return response.data
    except Exception as e:
        logger.error(f"Erro ao buscar contatos: {e}")
        return []

def send_message(phone, name):
    message = f"Olá, {name} tudo bem com você?"
    url = f"{ZAPI_API_URL}/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_API_TOKEN}/send-text"
    payload = {"phone": phone, "message": message}
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Mensagem enviada para {phone} ({name})")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Falha ao enviar para {phone} - {e}")
        return False

def main():
    logger.info("Iniciando envio de mensagens...")
    contacts = fetch_contacts(limit=3)
    if not contacts:
        logger.warning("Nenhum contato encontrado na tabela.")
        return
    sent_count = 0
    for contact in contacts:
        phone = contact.get("phone") or contact.get("phone_number")
        name = contact.get("name") or contact.get("nome")
        if not phone or not name:
            logger.warning(f"Contato com dados incompletos: {contact}")
            continue
        if send_message(phone, name):
            sent_count += 1
    logger.info(f"Processo concluído. {sent_count} mensagens enviadas.")

if __name__ == "__main__":
    main()