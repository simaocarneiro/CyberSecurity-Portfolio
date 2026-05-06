import socket
import logging
from datetime import datetime

# Configuração do ficheiro de log
logging.basicConfig(filename="honeypot_log.txt", level=logging.INFO, format='%(message)s')

def start_honeypot(host="0.0.0.0", port=8080):
    # Criar um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[*] Honeypot ativo na porta {port}...")
    print("[*] À espera de intrusos... (Ctrl+C para parar)")

    while True:
        # Aceitar a ligação do "atacante"
        client_socket, client_address = server_socket.accept()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Tentativa de invasão detetada de: {client_address[0]}:{client_address[1]}"

        print(f"\a[!] ALERTA: {log_entry}") # \a faz um som de bip no terminal
        logging.info(log_entry)

        # Enviar uma mensagem falsa para enganar o atacante
        client_socket.send(b"Access Denied. Unauthorized login attempt has been logged.\n")
        client_socket.close()

if __name__ == "__main__":
    try:
        start_honeypot()
    except KeyboardInterrupt:
        print("\n[!] Honeypot desligado. Verifica o ficheiro honeypot_log.txt.")
