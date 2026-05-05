# Projeto 05: Digitalização de Vulnerabilidades de Rede (Nmap)

## Descrição do Projeto
Este projeto foca-se na fase de **Reconhecimento Ativo**. Utilizei **Nmap**
(Network Mapper) para auditar o meu servidor Ubuntu, mapeando a superfície de
ataque através da descoberta de portas aberta e identificação detalhada de
serviços e versões.

Este laboratório demonstra competências em:
* Descoberta de ativos e mapeamento de rede.
* Identificação de versões de serviços (Banner Grabbing).
* Análise de serviços desconhecidos e assinaturas de fingerprinting.

---

## Ferramentas Utilizadas
* **Kali Linux:** Máquina de auditoria.
* **Nmap:** Ferramenta padrão para exploração de rede.
* **Ubuntu Server:** O alvo configurado (IP: 10.0.2.16).

---

## Execução Técnica
Foi executado um scan exaustivo para identificar todos os serviços expostos no alvo:

```bash
sudo nmap -sV -O -p- 10.0.2.16
```

## Análise dos resultados obtidos:
* **Porta 22 (SSH):** Versão OpenSSH 10.2p1 detetada.
* **Porta 80 & 3000:** Servidores web (Apache e Node.js Express) ativos.
* **Portas Altas (9090, 10250-25000):** Identificação de APIs em Golang e instâncias InfluxDB.
* **OS Detection:** Confirmado o uso de kernel Linux (Ubuntu).

## Evidência do Scan
A imagem em anexo demonstra o "output" do Nmap, revelando a complexidade dos serviços a correr no servidor.

## Conclusão Técnica
A realização de um scan completo (-p-) provou ser essencial, pois revelou serviços críticos
em portas não convencionais (acima de 100000). Esta informação é vital para um analista de
segurança decidir quais as superfícies de ataque que devem ser fechadas ou protegidas por
firewall.
