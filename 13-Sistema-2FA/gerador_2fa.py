import pyotp
import time

# 1. Gerar uma chave secreta aleatória (o que o site guarda no perfil do user)
# Em sistemas reais, esta chave é passada para o user via QR Code
secret = pyotp.random_base32()
print(f"CHAVE SECRETA PARTILHADA: {secret}")

# 2. Configurar o gerador TOTP (Time-based One-Time Password)
totp = pyotp.TOTP(secret)

print("\n--- SIMULADOR DE AUTENTICAÇÃO 2FA ---")
print("O código abaixo expira a cada 30 segundos.\n")

# 3. Mostrar o código a mudar em tempo real
try:
    for i in range(5):
        print(f"Código Atual: {totp.now()}")
        print("A aguardar 10 segundos para a próxima verificação...")
        time.sleep(10)
except KeyboardInterrupt:
    print("\n[!] Simulação terminada.")
