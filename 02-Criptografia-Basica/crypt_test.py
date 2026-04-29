from cryptography.fernet import Fernet

#1. Gerar uma chave
chave = Fernet.generate_key()
cipher = Fernet(chave)

#2. Definir a mensagem
mensagem = "Criptografia basica concluida com sucesso!". encode()

#3. Criptografar
texto_cifrado = cipher.encrypt(mensagem)

print("-" * 30)
print("CHAVE GERADA:", chave.decode())
print("-" * 30)
print("MENSAGEM CRIPTOGRAFADA:")
print(texto_cifrado.decode())
print("-" * 30)

#4. Descriptografar para provar que funciona
texto_original = cipher.decrypt(texto_cifrado)
print("MENSAGEM ORIGINAL REVELADA:")
print(texto_original.decode())
print("-" * 30)
