# Projeto 13: Implementação de Sistema 2FA (TOTP)

## Visão Geral
Este projeto demonsta o funcionamento técnico de sistemas de Autenticação de Dois Fatores (2FA) baseados em tempo (**TOTP - Time-based One-Time Password**). É a mesma tecnologia utilizada por aplicações como o Google Authenticator ou
Authy para gerar códigos de segurança temporários.

## Como funciona o Algoritmo TOTP?
O sistema baseia-se em dois pilares fundamentais:
1. **Chave Secreta (Shared Secret):** Uma string aleatória em Base32 partilhada entre o servidor e o dispositivo do utilizador (geralmente via QR Code).
2. **Sincronização por Tempo:** O algoritmo utiliza o *Unix Timestamp* atual dividido por intervalos de 30 segundos.

O resultado é um hash que é truncado para gerar um código numérico de 6 dígitos. Como ambos os lados têm a chave e o tempo está sincronizado, ambos geram o mesmo número sem precisar de comunicar entre si no momento do login.



## Tecnologias Utilizadas
* **Python3**: Linguagem principal.
* **PyOTP**: Biblioteca padrão para implementação de TOTP (RFC 6238).
* **Time**: Módulo nativo para gestão dos intervalos de expiração.

## Implementação
O script 'gerador_2fa.py' realiza os seguintes passos:
1. Gera uma chave secreta única.
2. Inicia um loop que consulta o token atual a cada 10 segundos.
3. Demonstra a persisência do código durante a janela de 30 segundos e a sua alteração imediata após esse período.

## Importância para a Cibersegurança
A implementação de 2FA é uma das camadas de defesa mais eficazes contra:
* **Phishing:** Mesmo que a password seja roubada, o atacante não tem o token físico.
* **Brute Force:** O código muda demasiado rápido para ser adivinhado por tentativa e erro.
* **Credential Stuffing:** Passwords reutilizadas de fugas de dados tornam-se inúteis sem o segundo fator.


