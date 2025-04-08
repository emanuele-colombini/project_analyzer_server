
import re

def read_markdown_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Errore: Il file {file_path} non è stato trovato.")
        return ""
    except Exception as e:
        print(f"Errore nella lettura del file {file_path}: {e}")
        return ""


def sanitize_folder_name(name: str) -> str:
    
    # Rimuove caratteri non alfanumerici (tranne spazi e underscore)
    sanitized = re.sub(r'[^\w\s]', '', name)
    
    # Sostituisce spazi con underscore
    sanitized = sanitized.replace(' ', '_')
    
    # Rimuove underscore multipli consecutivi
    sanitized = re.sub(r'_+', '_', sanitized)
    
    # Rimuove underscore all'inizio e alla fine
    sanitized = sanitized.strip('_')
    
    # Converte tutto in minuscolo per uniformità
    sanitized = sanitized.lower()
    
    # Se il nome è vuoto dopo la sanitizzazione, restituisce un valore predefinito
    if not sanitized:
        sanitized = "unknown_project"
    
    return sanitized
