import os
import subprocess

def run_vuln_scan(target):
    print(f"--- A iniciar scanner de vulnerabilidades em: {target} ---")
    print("Isso pode demorar alguns minutos dependendo dos serviços...\n")

    # Comando Nmap que usa scripts de vulnerabilidades (vukn)
    # -sV: Deteta versões dos serviços
    # --script vuln: Corre a categoria de scripts de vulnerabilidades
    command = ["nmap", "-sV", "--script", "vuln", target]

    try:
        # Executa o comando e captura a saída
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print("Scan Concluído com Sucesso!\n")
            print("--- RESULTADOS ---")
            print(result.stdout)

            # Guardar num ficheiro para o relatório do projeto
            with open("scan_report.txt", "w") as f:
                f.write(result.stdout)
            print("\n Relatório guardado em 'scan_report.txt'")
        else:
            print("Erro ao executar o Nmap. Verifica se tens permissões de sudo.")

    except FileNotFoundError:
        print("Nmap não encontrado. Instala com: sudo apt install nmap")

if __name__ == "__main__":
    alvo = input("Insere o IP ou domínio para scan (ex: 127.0.0.1): ")
    run_vuln_scan(alvo)
