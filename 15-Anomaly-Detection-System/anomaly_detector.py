import time
import os

# Configurações
LOG_TO_WATCH = "keylog.txt"
ALERTA_FICHEIRO = "alertas_segurança.txt"
PALAVRAS_CHAVE = ["password", "login", "admin", "root", "iban", "cvv"]
LIMITE_CARACTERES = 100 # Se houver mais de 100 caracteres novos entre verificações

def analisar_logs():
    print(f"Sistema de Deteção de Anomalias ativo no ficheiro: {LOG_TO_WATCH}")
    ultima_posicao = 0

    while True:
        if os.path.exists(LOG_TO_WATCH):
            with open(LOG_TO_WATCH, "r") as f:
                # Vai para onde parou na última vez
                f.seek(ultima_posicao)
                novos_dados = f.read()
                ultima_posicao = f.tell()

                if novos_dados:
                    # 1. Detetar volume anormal (Flood)
                    if len(novos_dados) > LIMITE_CARACTERES:
                        gerar_alerta(f"VOLUME ANORMAL: {len(novos_dados)} caracteres detetados de uma vez!")

                    # 2. Detetar palavras sensíveis
                    for palavra in PALAVRAS_CHAVE:
                        if palavra in novos_dados.lower():
                            gerar_alerta(f"DADOS SENSÍVEIS: Palavra-chave '{palavra}' detetada no log!")

    time.sleep(5) # Verifica a cada 5 segundos

def gerar_alerta(mensagem):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    alerta_formatado = f"[{timestamp}] {mensagem}\n"
    print(alerta_formatado)
    with open(ALERTA_FICHEIRO, "a") as f:
        f.write(alerta_formatado)

if __name__ == "__main__":
    analisar_logs()
