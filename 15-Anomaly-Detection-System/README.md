# Projeto 15: Anomaly Detection System (ADS)

## Visão Geral
Este projeto consiste num sistema de monitorização e deteção de anomalias em tempo real desenvolvido em Python. O objetivo é analisar ficheiros de log continuamente para identificar atividades suspeitas, acessos indevidos a dados
sensíveis ou volumes anormais de tráfego que possam indicar ataques automatizados ou exfiltração de informação.

## Funcionalidades
* **Monitorização Incremental:** O script utiliza um sistema de leitura inteligente ('f.seek'), processando apenas os dados novos adicionados ao log para otimizar o desempenho do sistema.
* **Deteção Baseada em Assinaturas:** Identifca proativamente palavras-chave críticas (ex: 'passord', 'admin', 'login', 'root') no fluxo de dados.
* **Análise Heurística de Volume:** Deteta picos súbitos de escrita. Se um volume de caracteres ultrapassar o limite definido num curto espaço de tempo, o sistema dispara um alerta de "Volume Anormal".
* **Registo de Incidentes:** Todos os alertas são apresentados no terminal e guardados num ficheiro histórico ('alertas_seguranca.txt') com a respetiva data e hora (timestamp).

## Lógica de Funcionamento
O sistema opera num ciclo contínuo (polling) que verifica o ficheiro alvo a cada 5 segundos:
1. **Identificação de Dados Novos:** O script compara o tamanho real do ficheiro com a última posição lida.
2. **Triagem de Volume:** Se o bloco de novos dados for desproporcionalmente grande, é classificado como anomalia de volume.
3. **Varredura de Padrões:** O conteúdo é convertido para minúsculas e comparado com uma lista de termos sensíveis pré-definidas.
4. **Resposta:** Caso alguma condição seja cumprida, o sistema executa a função de alerta.

## Tecnologias Utilizadas
* **Python 3**: Linguagem base para a lógica de deteção.
* **OS & Time Modules**: Para manipulação de ficheiros, gestão de caminhos e controlo de intervalos de tempo.
