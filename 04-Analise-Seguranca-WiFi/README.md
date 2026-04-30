# Projeto 04: Análise de Segurança Wifi

## Descrição do Projeto
Este laboratório foca-se nos fundamentos da auditoria de redes sem fios (WLAN).
O objetivo principal foi compreender o funcionamento da suite **Aircrack-ng**
e o processp de preparação de uma interface de rede para a monitorização e
captura de pacotes em ambientes WiFi.

Este projeto demonstra competências em:
* Utilização de ferramentas de auditoria wireless no Kali Linux.
* Compreensão da arquitetura de rede 802.11.
* Preparação de sistemas para testes de intrusão em redes sem fios.

---

## Ferramentas Utilizadas
* **Kali Linux:** Máquina de ataque.
* **Airmon-ng:** Ferramenta utilizada para gerir modos de interface e verificar a
compatibilidade do hardware para o modo monitor.


---

## Metodologia e Execução
O primeiro passo de uma análise WiFi profissional consiste em identificar as 
interfaces disponíveis e verificar se as mesmas suportam o **Modo Monitor**.

Foi utilizado o comando:
```bash
sudo airmon-ng
```
Esta fase é crítica porque, sem a ativação do modo monitor, a placa de rede ignora todos os
pacotes que não sejam destinados especificamente ao nosso endereço MAC, impossibilitando
a captura de "Handshakes" ou a análise de tráfego de outros dispositivos na rede.

## Resultados e Observações
A imagem em anexo demonstra a execução do comando inicial de reconhecimento de hardware.

Nota: Em ambientes de Máquina Virtual (VM), o hardware wireless é frequentemente simulado
como Ethernet, o que requer hardware externo (adaptador USB WiFi) para a execução
completa da captura de pacotes em modo monitor.
