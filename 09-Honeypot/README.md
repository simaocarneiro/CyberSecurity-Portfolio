# Projeto 09: Implementação de um Honeypot de Baixa Interação

## Visão Geral
Este projeto consiste na criação de um **Honeypot** (pote de mel) básico desenvolvido
em Python. O objetivo é simular um serviço vulnerável numa rede para atrair, detetar e
registar tentativas de acesso não autorizado por parte de agentes maliciosos.

---

## O que é um Honeypot?
Um honeypot é um recurso de segurança informática (servidor, aplicação ou dados)
desenhado especificamente para ser sondado, atacado ou comprometido.

### Objetivos Principais:
* **Deteção Precoce:** Identificar atividades de reconhecimento antes que o atacante encontre sistemas reais.
* **Recolha de Inteligência:** Registar os endereços IP dos atacantes e os métodos de interação utilizado.
* **Diversão de Recursos:** Manter o atacante ocupado num sistema isolado e sem valor real.

---

## Demonstração Técnica (PoC)

Nesta implementação, o script 'honeypot.py' abre um socket TCP na porta **8080** (comumente usada para serviços web alternativos ou proxies).

### Fluxo do Ataque Simuladdo:
1. **Execução:** O Honeypot é ativado e fica "à escuta".
2. **Tentativa de Ligação:** Utilizando a ferramenta 'netcat' (nc), simulammos um atacante a tentar aceder à porta aberta.
3. **Resposta e Registo:** O Honeypot envia uma mensagem de erro genérica ("Access Denied") para manter a ilusão, enquanto regista simultaneamente o IP
e o timestamp do incidente num ficheiro de log.

### Evidências:
* **Log Gerado:** O ficheiro 'honeypot_log.txt' armazena o histórico de todas as interações.
* **Alerta em Tempo Real:** O terminal exibe um alerta visual assim que a ligação é estabelecida.

---

## Valor para o Portfólio de Cibersegurança
A implementação de Honeypots visa a demonstração de conhecimento avançaado de **Defesa Ativa**. Em vez de uma postura puramente reativa, este projeto
mostra como um analista de segurança pode criar armadilhas para obter vantagem tática sobre um atacante.

**Nota:** Este projeto foi realizado em ambiente de rede local controlada para fins educativos. O uso de Honeypots em ambientes corporativos requer
planeamento para evitar que o próprio Honeypot seja usado como um ponto de salto para a rede interna.
