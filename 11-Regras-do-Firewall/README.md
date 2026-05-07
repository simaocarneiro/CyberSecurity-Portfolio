# Projeto 11: Configuração de Regras de Firewall (Hardening)

## Visão Geral
Este projeto demonstra a implementação de uma política de segurança rigorosa utilizando o **UFW (Uncomplicated Firewall)**. O objetivo é reduzir a
superfície de ataque do sistema, aplicando o conceito de **Default Deny**.

## Estratégia de Defesa
Em vez de permitir todo o tráfego e bloquear apenas o que é mau, esta configuração inverte a lógica:
1. **Bloqueio Total:** Todo o tráfego de entrada (Inbound) é bloqueado por defeito.
2. **Exceções Necessárias:** Apenas as portas essenciais (SSH, HTTP, HTTPS) são abertas manualmente.
3. **Segurança de Saída:** O tráfego de saída (Outbound) é permitido para garantir atualizações e navegação.

## Implementação
Foi desenvolvido um script em Shell ('configurar_firewall.sh') que automatiza:
* O reset de regras anteriores.
* A definição das políticas padrão.
* A abertura controlada das portas 22, 80 e 443.

---
> **Nota de Segurança:** Esta configuração é um passo fundamental no *Server Hardening*, garantindo que serviços não documentados não fiquem expostos a varrimentos de rede (scnas).
