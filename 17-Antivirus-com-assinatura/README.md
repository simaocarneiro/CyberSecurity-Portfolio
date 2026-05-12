# Projeto 17: Antivirus with Signatures (AV)

## Descrição
Desenvolvimento de um motor de antivírus baseado em assinaturas (Static Analysis). O sistema utiliza o algoritmo de hashing **SHA-256** para identificar ficheiros maliciosos comparando-os com uma base de dados de ameaças conhecidas.

## Funcionalidades
* **Recursive Scanning:** Varre subdiretórios à procura de ficheiros.
* **Hash validation:** Gera assinaturas únicas para cada ficheiro, independentemente da extensão.
* **Incident Reporting:** Reporta o nome do ficheiro, o tipo de malwware associado e assinatura detetada.

## Como Testar
1. Colocar ficheiros no diretório './diretorio_teste'.
2. Executar 'python3 antivirus.py'.
3. Para simular um positivo, criar um ficheiro cujo conteúdo gere um hash presente na 'MALWARE_DB'.
