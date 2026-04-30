# Projeto 03: Teste de Força Bruta via SSH (Hydra)

## Descrição do Projeto
Este laboratório demonstra como um atacante pode explorar credenciais fracas
utilizando ataques de **Brute Force**. O objetivo foi realizar um teste controlado
entre duas máquinas virtuais (Kali Linux e Ubuntu Server) para identificar vulnerabilidades
no serviço SSH.

Este projeto demonstra competências em:
* Utilização da ferramenta **Hydra**.
* Testes de penetração em serviços de rede.
* Identificação de falhas de autenticação.

---

## Ferramentas Utilizadas
* **Kali Linux:** Máquina de ataque.
* **Ubuntu Server:** Máquina alvo (Vítima).
* **Hydra:** Ferramenta de quebra de passwords rápida e flexível.

---

## Cenário de Execução
1. **Configuração do Alvo:** Criação de um utilizador de suporte com uma password vulnerável no Ubuntu Server.
2. **Wordlist:** Criação de uma lista de passwords prováveis.
3. **Execução:**
	```bash
	hydra -l suporte -P passwords.txt ssh://10.0.2.12
	```
## Resultados (Prova de Conceito)
O ataque foi bem-sucedido, tendo o Hydra identificado a password em poucos segundos devido à baixa complexidade da mesma.

## Como Prevenir?
Para mitigar este tipo de ataque, aprendi que as seguintes medidas são essenciais:
- Utilizar **passwords fortes** e complexas.
- Implementar o **Fail2Ban** para bloquear IPs após várias tentativas falhadas.
- Utilizar **Chaves SSH** (Public Key Auth) em vez de passwords.
- Alterar a porta padrão do SSH (22).
