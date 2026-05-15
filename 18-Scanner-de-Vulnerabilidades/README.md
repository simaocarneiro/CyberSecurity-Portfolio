# Projeto 18: Vunerability Scanner Automator

## Descrição
Este projeto consiste num automatizador de scans de vulnerabilidades desenvolvido em Python, utilizando o motor **NSE (Nmap Scripting Engine)**. O script foca-se na deteção de **CVEs** (Common Vulnerabilities and Exposures) e falhas
de configuração em serviços de rede.

## Funcionalidades
* **Fingerprinting de Serviços:** Identifica versões exatas de software (HTTP, SSH, FTP, etc.).
* **Vulnerability Mapping:** Corre scripts específicos da categoria 'vuln' do Nmap.
* **Auto-Reporting:** Gera automaticamente um ficheiro 'scan_report.txt' com os achados.

## Como executar
1. 'sudo python3 vuln_scanner.py''
2. Introduzir o IP alvo.
3. Analisar o relatório gerado.

---

## Resultaddos do Scan (Metasploitable 3 - Windows Server)

O relatório gerado pelo motor NSE (Nmap Scripting Engine) expôs uma superfície de ataque massiva, categorizada em falhas de infraestrutura, exploits críticos de execução remota de código (RCE) e fugas severas de informação.

### 1. Vulnerabilidades Críticas de Infraestruturas e Serviços
O scanner mapeou múltiplos serviços desatualizaos associados a exploits públicos com pontuação máxima de severidade (**CVSS 9.8 a 10.0**):
* **Porta 21/TCP (FTP):** Identificado o serviço 'Microsoft ftpd'.
* **Porta 22/TCP (SSH):** Detetada a versão 'OpenSSH 7.1'. O motor listou dezenas de exploits conhecidos de execução remota e bypass (com referências diretas para *Packet Storm*, *Exploit-DB* e *CVEs* recentes).
* **Porta 80/TCP (HTTP):** Servidor 'Microsoft IIS httpd 7.5' exposto com vulnerabilidades severas, incluindo exploits de **Denial of Service (DoS)** e vetor 'MS10-065' (ligado a vulnerabilidades em ASP.NET).
* **Portas 135, 139 e 445/TCP:** Serviços nativos do ecossistema Windows ('RPC', 'NetBIOS-SSN' e 'Micrososft-DS' para Windows Server 2008 R2 / 2012) ativos e vulneráveis a enumeração.
* **Porta 3306/TCP (MySQL):** Correndo a versão 'MySQL 5.5.20-log', vulnerável ao 'CVE-2017-15945'.

### 2. Enumeração Massiva de Diretórios e Painéis Administrativos
O script executou um ataque de força bruta estruturado aos caminhos do servidor web, revelando uma arquitetura completamente desprotegida:
* **Painéis de Controlo de Bases de Dados:** Exposição de caminhos críticos como '/phpmyadmin/', '/mysql/' e subpastas de gestão de dados.
* **Acesso a CMS e Frameworks:** Identificação de instalações ativas do '/wordpress/', '/joomla/administrator/', '/cgi-bin/mj_wwwusr' (Majordomo), '/tikiwiki/' e instâncias do 'Oracle J2EE'.
* **Pastas Administrativas Suspeitas:** Descoberta de centenas de diretórios previsíveis do sistema como '/admin/', '/administrator/', '/manager/', '/webadmin/', '/bb-admin/', '/controlpanel/' e as suas respetivas variantes em extensões
'.php', '.apsx', '.cfm', '.html' e '.asp'.

### 3. Backdoors e Fugas de Informação (Information Disclosure)
O scanner confirmou a existência de pontos de entrada arbitrários e ficheiros sensíveis expostos no servidor:
* **Deteção de Web Shells / Backdoors:** Mapeamento de vetores de execução direta em caminhos como '/shell', '/cmd', '/cmd.aspx' e '/exectest'.
* **Ficheiros de Configuração e Backups:** Exposição de ficheiros críticos contendo potencialmente credenciais ou logs, através de caminhos como '/config.php', '/setup.php', '/install.php' e arquivos '.bak' ou '.log'.
* **Vulnerabilidades Web (Aplicações):** Confirmação de falhas do tipo **Cross-Site Request Forgery (CSRF)** e falta de mecanismos de proteção contra injeções nas páginas enumeradas.
