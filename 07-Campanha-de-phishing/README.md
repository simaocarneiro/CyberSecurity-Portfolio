# Projeto 07 - Campanha de phishing (Credential Harvesting)

Este projeto demonstra a execução de um ataque de engenharia social para captura
de credenciais utilizando o **Social-Engineer Toolkit (SET)** no Kali Linux.

## Ferramentas e Tecnologias
* **Kali Linux:** Sistema operativo utilizado.
* **Social-Engineer Toolkit (SET):** Framework de automação de ataques.
* **Web Templates:** Clonagem automatizada da interface de login do Google.

## Passo a Passo (Execução)

1. **Início do SET:**
   ```bash
   sudo setoolkit
   ```
2. Configuração do Vetor de Ataque:
* Escolha da opção **1) Social-Engineering Attacks.**
* Escolha da opção **2) Website Attack Vectors**.
* Escolha da opção **3) Credential Harvester Attack Method**.

3. Lançamento da Página Falsa:
* Seleção de **1) Web Templates**.
* Condfirmação do endereço IP da máquina local para o POST dos dados.
* Seleção do template **2) Google**.

4. Captura de Dados:
* O servidor aguarda que o alvo insira os dados no endereço IP do atacante.
* As credenciais são exibidas em texto simples diretamente no terminal.

## Resultados
O ataque foi bem-sucedido, permitindo a visualização imediata do email e da password assim
que o formulário foi submetido na página clonada.

## Mitigação
* Implementação de **Autenticação Multi-fator (MFA)**.
* Treino de consciencialização para verificação de URLs antes de submeter dados sensíveis.
