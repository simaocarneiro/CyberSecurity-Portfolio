# Projeto 01: Configuração de Home Lab de Cibersegurança

## Descrição
Este projeto consistiu na criação de um ambiente isolado e seguro para a prática de testes de penetração e análise de segurança, garantindo que as atividades não afetem redes externas.

## Topologia do Laboratório
- **Hipervisor:** VirtualBox
- **Máquinas Atacantes:** - Kali Linux (Distribuição principal equipada com ferramentas de Penetration Testing.)
	- Kali Purple (Variante focada em operações defensivas (Blue Team) e monitoramento de segurança.)
- **Máquinas Vítimas:**
	- Metaslpoitable 2 (Máquina Linux propositadamente vulnerável para exploração de serrviços básicos.)
	- Metasploitable 3 (Windows Server & Ubuntu: Versões mais modernas que simulam vulnerabilidades em ambientes Windows Server e Linux.)
	- Ubuntu Desktop (Utilizado para simular o comportamento de uma estação de trabalho de um utilizador final e testar ataques de engenharia social.)
	- Ubuntu Server (Utilizado para simular um servidor de produçãoo,, permitindo a prática de endurecimento de sistemas (hardening) e análise  de logs de serviços reais.

## Configuração de Rede
- Tipo: Rede NAT
- Objetivo: Permitir que as máquinas virtuais comuniquem entre si (essencial para testes de penetração) e, simultaneamente, tenham acesso à internet para atualização de pacotes e ferramentas, mantendo uma camada de separação da
  rede do hospedeiro (host).
