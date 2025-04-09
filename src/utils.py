import os
import re

def read_markdown_file(file_path: str) -> str:
    try:
        file_path = os.path.join(
            os.getcwd(),
            file_path
        )
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
    sanitized = sanitized.replace(' ', '_')
    sanitized = re.sub(r'_+', '_', sanitized)
    sanitized = sanitized.strip('_')
    sanitized = sanitized.lower()
    
    # Se il nome è vuoto dopo la sanitizzazione, restituisce un valore predefinito
    if not sanitized:
        sanitized = "unknown_project"
    
    return sanitized
