# Projeto 16: Snort IDS (Intrusion Detection System)

## Visão Geral
Este projeto demonstra a implementação e configuração do **Snort 3**, um Sistema de Deteção de Intrusão (IDS) de nova geração. O objetivo é monitorizar
o tráfego de rede em tempo real para identificar padrões de ataque, como varreduras de portas (Port Scanning) e tentativas de reconhecimento (ICMP Pings).

## Arquitetura e Configuração
* **Motor:** Snort 3.0 (utilizando configuração baseada em Lua).
* **Ficheiro de Configuração:** '/etc/snort/snort.lua'.
* **Base de Regras:** Implementação de regras personalizadas no ficheiro 'local.rules' para deteção de assinaturas específicas.

## Regras Implementadas
Foram criadas e validadas as seguintes assinaturas de deteção:
1. **Deteção de ICMP (Ping):** Identifica pedidos de eco ICMP, frequentemente usados para mapear hosts ativos na rede.
2. **Deteção de TCP SYN Scan:** Identifica tentativas de varredura furtiva (Stealth Scan) através da monitorização de pacotes com a flag 'SYN' ativa em
direção ao host.


## Resultados Obtidos
Durante os testes de stress utilizando o 'Nmap', o Snort 3 foi capaz de:
* Intercetar todos os pacotes de sondagem.
* Gerar alertas em tempo real no modo 'alert_fast'.
* Identificar corretamente o IP de origem e os serviços alvo do atacante.

## Comandos Utilizados
Para iniciar a monitorização:
```bash
sudo snort -c /etc/snort/snort.lua -R /etc/snort/rules/local.rules -i eth0 -A alert_fast
```
