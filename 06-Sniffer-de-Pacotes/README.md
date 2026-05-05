# Projeto 06: Sniffer de pacotes (análise de protocolos)

## Descrição do Projeto
Este projeto demonstra a capacidade de intercetar e analisar tráfego de rede em
tempo real. O **Packet Sniffing** é uma técnica fundamental tanto para administradores
de rede (troubleshooting) como para analistas de segurança (deteção de intrusões
e análise de malware).

Este laboratório demonstra competências em:
* Captura de pacotes em modo promíscuo.
* Análise de tráfego em baixo nível (Hexadecimal e ASCII).
* Utilização da ferramenta de linha de comando **tcpdump**.

---

## Ferramentas Utilizadas
* **Kali Linux:** Máquina de monitorização.
* **tcpdump:** Analisador de pacotes profissional.
* **Protocolos analisados:** ICMP (Ping) e tráfego TCP/IP geral.

## Execução Técnica
Foi realizada uma captura seletiva de pacotes na interface de rede para observar
a estrutura dos dados que circulam entre o atacante e o alvo:

```bash
sudo tcpdump -i eth0 -xx -c 10
```

## O que foi observado:
* **Cabeçalhos IP:** Identificação das origens e destinos.
* **Payload:** Visualização dos dados brutos em formato hexadecimal, permitindo identificar
se a informação está a ser enviada de forma cifrada ou em texto simples.

## Evidência da Captura
A imagem em anexo mostra o momento em que os pacotes foram intercetados e "desmontados"
no terminal.

## Conclusão Técnica
O sniffing de pacotes revela a fragilidade de protocolos não cifrados. Através desta prática,
torna-se evidente que sem a utilização de protocolos como HTTPS ou SSH, qualquer atacante
na mesma rede poderia ler informações sensíveis diretamente dos pacotes capturados.
