import hashlib
import os

# 1. Nossa "Blacklist" de Malware (Hashes SHA-256 de exemplo)
# Na vida real, esta listas têm milhões de entradas.
MALWARE_DB = {
    "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8": "Trojan.Generic.Kali",
    "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824": "Spyware.PasswordStealer",
    "81381229312713d2d5594190607f289d14006505962d44863e46d5f75973e461": "Ransomware.Test"
}

def get_file_hash(filepath):
    """Calcula o SHA-256 de um ficheiro de forma eficiente."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return None

def scan_folder(path):
    print(f"--- Scanner de Malware Iniciado: {path} ---")
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            f_hash = get_file_hash(full_path)

            if f_hash in MALWARE_DB:
                print(f"\n[ALERTA] MALWARE DETETADO!")
                print(f"Ficheiro: {file}")
                print(f"Ameaça: {MALWARE_DB[f_hash]}")
                print(f"Hash: {f_hash}")
                print("-" * 45)
            else:
                print(f"[OK] {file}: Limpo", end="\r")

if __name__ == "__main__":
    # Vamos fazer scan a uma pasta de testes
    scan_folder("./diretorio_teste")
